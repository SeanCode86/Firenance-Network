# * ----------------------------------------------------------------------------- * #
"""
        This is the Firefly! Financial App, and a way for users to to check
        their investments, it will be the user interface to mine firecoins.
        This is just a prototype for a instance of the FireBot API-Platform.
        It is just the wep app implementation of it. FireBot API will be built
        properly with the help if POSTMAN API builder, or FastAPI. I thinking
        the asynchronous nature of FastAPI, will be a better way to build webhooks

"""
# * ----------------------------------------------------------------------------- * #
import pandas as pd
import yfinance as yf    # For now we just use Yahoo Finance API
import streamlit as st   # The framwork used to build the Pythonic Web App
import datetime as dt
import plotly.graph_objs as go # What we use to build our graphs
from plotly.subplots import make_subplots # And for subplots, to be build along graph objects

snp500 = pd.read_csv("Datasets/sp500.csv")         # Our CSV FILE to parse
symbols = snp500["Symbol"].sort_values().tolist()  # List SP500 Companies in Alphabetical Order


# * ----------------------------------------------------------------------------- * #
def main():

    # * --------------------------------------------- * #
    """ Put Metadata code here in to pYthon wrapper function"""
    # * --------------------------------------------- * #

    # This will build a drop-down list in streamlit
    ticker = st.sidebar.selectbox(
        "Choose a S&P 500 Stock",
            symbols
    )

    # We give the Web User two contexts of fincial data from data set
    infoType = st.sidebar.radio(
        "Choose an Info Type",
            ("Fundamental",    # Will build a basic plot
             "Technical"       # More technical plot with subplots
             )
    )

    # We do the same thing as Above, except using a cryptocurrency data set
    crypto_sym = st.sidebar.selectbox(
        "Choose a cryptocurrency",
        symbols     # toDO --> Must make the same thing work with diffirent data set
    )

    infoType_crypto = st.sidebar.radio(
        "Choose Internet Paradigm of Crypto currency",

        ("Stabelcoin",
         "DeFi",
         "ERC-20",
         "NFT",
         "DOT Ecosystem",
         "BSC Ecosystem",
         "ZIL Ecosystem",
         "Meme Coin",
         "Avalanche Ecosystem",
         "Chillz Ecosystem",
         "Solana Ecosystem",
         "Tezos Ecosystem",
         "Terra Ecosystem",
         "Polygon Ecosystem",
         "Algorand Ecosystem")
    )


    # * ------------------------------------------------------------- * #
    #                THIs enables the viewer to toggle between
    #                the Radion buttons. This controls what happens
    #                In the SIDEBAR
    # * ------------------------------------------------------------- * #

    # Conditional to enable selection of radio buttons
    if (infoType == "Fundamental"):

        stock = yf.Ticker(ticker)
        info = stock.info

        # Our Python script to dislplay Streamlit stuff, here we get
        # our data to build this from Yahonn Finance API
        st.title("Company Profile")
        st.subheader(info['longName'])

        st.markdown('** Sector **: ' + info['sector'])
        st.markdown('** Industry **: ' + info['industry'])
        st.markdown('** Phone **: ' + info['phone'])

        st.markdown('** Address **: ' + info['address1'] + ', '
                    + info['city'] + ', '
                    + info['zip'] + ', '
                    + info['country']
        )

        st.markdown('** Website **: ' + info['website'])
        st.markdown('** Business Summary **')
        st.info(info['longBusinessSummary'])

        # Our JSON Dictionary data structure

        fundInfo = {
            'Enterprise Value (USD)': info['enterpriseValue'],
            'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
            'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
            'Net Income (USD)': info['netIncomeToCommon'],
            'Profit Margin Ratio': info['profitMargins'],
            'Forward PE Ratio': info['forwardPE'],
            'PEG Ratio': info['pegRatio'],
            'Price to Book Ratio': info['priceToBook'],
            'Forward EPS (USD)': info['forwardEps'],
            'Beta ': info['beta'],
            'Book Value (USD)': info['bookValue'],
            'Dividend Rate (%)': info['dividendRate'],
            'Dividend Yield (%)': info['dividendYield'],
            'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
            'Payout Ratio': info['payoutRatio']
        }

        fundDF = pd.DataFrame.from_dict(
            fundInfo, orient= "index"
        )

        fundDF = fundDF.rename(
            columns = {0: "Value"}
        )

        st.subheader("Fundamental Info")
        st.table(fundDF)

        # This will graph the growth of a selected stock ticker over the
        # last two years

        st.subheader('General Stock Info')

        # Our Streamlit Python Script to define markuped Parsing

        st.markdown('** Market **: '
                    + info['market']
        )

        st.markdown('** Exchange **: ' +
                    info['exchange']
        )

        st.markdown('** Quote Type **: ' +
                    info['quoteType']
        )

        # Our starting and finisjing parameter to make up graph
        start = dt.datetime.today() - dt.timedelta(2 * 365)
        end = dt.datetime.today()

        # And use our Python library to scrape the data
        df = yf.download(
            ticker,
                start,
                    end
            )

        df = df.reset_index()

        # Plot our graph
        fig = go.Figure(

            data = go.Scatter(
                x = df["Date"],
                y = df["Adj Close"]
            )
        )

        fig.update_layout(
            title = {
                'text': "Stock Prices Over Past Two Years",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

        st.plotly_chart(fig,
                        use_container_width = True
        )

        marketInfo = {
            "Volume": info['volume'],
            "Average Volume": info['averageVolume'],
            "Market Cap": info["marketCap"],
            "Float Shares": info['floatShares'],
            "Regular Market Price (USD)": info['regularMarketPrice'],
            'Bid Size': info['bidSize'],
            'Ask Size': info['askSize'],
            "Share Short": info['sharesShort'],
            'Short Ratio': info['shortRatio'],
            'Share Outstanding': info['sharesOutstanding']
        }

        marketDF = pd.DataFrame(
            data = marketInfo,
            index = [0]
        )

        st.table(marketDF)

    # * ------------------------------------------------------------- * #
    #                END of Fundamental Data toggle Condition
    # * ------------------------------------------------------------- * #

    # Else the user wants to see technical details
    # * ------------------------------------------------------------- * #
    #         Make Fourier Series Function, to display Technical
    #         Data Toggle of Radio Button
    # * ------------------------------------------------------------- * #
    else:

        def calcMovingAverage(data, size):
            df = data.copy()

            df['sma'] = df[
                'Adj Close'].rolling(
                size).mean()

            df['ema'] = df[
                'Adj Close'].ewm(
                span = size,
                min_periods = size).mean()

            df.dropna(inplace = True)
            return df

        def calc_macd(data):
            df = data.copy()

            df['ema12'] = df[
                'Adj Close'].ewm(
                span = 12,
                min_periods = 12
            ).mean()

            df['ema26'] = df[
                'Adj Close'].ewm(
                span = 26,
                min_periods = 26
            ).mean()

            df['macd'] = df[
                'ema12'] - df['ema26']

            df['signal'] = df['' \
                'macd'].ewm(
                span = 9,
                min_periods = 9
            ).mean()

            df.dropna(inplace=True)

            return df

        def calcBollinger(data, size):
            df = data.copy()

            df["sma"] = df[
                'Adj Close'].rolling(size
            ).mean()

            df["bolu"] = df[
                "sma"] + 2 * df[
                'Adj Close'].rolling(size
            ).std( ddof = 0)

            df["bold"] = df[
                "sma"] - 2 * df[
                'Adj Close'].rolling(
                size).std(ddof = 0)

            df["width"] = df["bolu"] - df["bold"]
            df.dropna(inplace=True)

            return df

        st.title("Technical Indicators")
        st.subheader("Moving Averages")

        coMA1, coMA2 = st.columns(2) # Split frame into 2 columns

        # In the first column
        with coMA1:

            numYearMA = st.number_input(
                'Insert period (Year): ',
                min_value = 1, max_value = 10,
                value = 2, key = 0)

        with coMA2:

           windowSizeMA = st.number_input(
               'Window Size (Day): ',
               min_value = 5, max_value = 500,
               value = 20, key = 1
           )

        start = dt.datetime.today() - dt.timedelta(
            numYearMA * 365
        )

        end = dt.datetime.today()
        dataMA = yf.download(
            ticker,
                start,
                    end
        )

        df_ma = calcMovingAverage(dataMA, windowSizeMA)
        df_ma = df_ma.reset_index()

        figMA = go.Figure()

        figMA.add_trace(

            go.Scatter(
            x = df_ma['Date'],
            y = df_ma['Adj Close'],
            name = "Prices Over Last " + str(numYearMA) + " Year(s)"
            )
        )

        figMA.add_trace(

            go.Scatter(
                x = df_ma['Date'],
                y = df_ma['sma'],
                name = "SMA" + str(windowSizeMA) +
                       " Over Last " + str(numYearMA) + " Year(s)"
            )
        )

        figMA.add_trace(

            go.Scatter(
                x = df_ma['Date'],
                y = df_ma['ema'],
                name = "EMA" + str(windowSizeMA) +
                       " Over Last " + str(numYearMA) + " Year(s)"
            )
        )

        figMA.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))

        figMA.update_layout(legend_title_text='Trend')
        figMA.update_yaxes(tickprefix="$")

        st.plotly_chart(figMA, use_container_width=True)
















       # * =========================================================================== * #
#                SACRIFICE and Main applications's main event loop
# * =========================================================================== * #

main()
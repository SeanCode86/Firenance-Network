# * ------------------------------------------------------------------------------- * #
"""
                This is the adminsitration interface of Firefly Ecosystem.py
                This is just something to help me monitor to the project
"""
# * ------------------------------------------------------------------------------- * #
# Our imports
import streamlit as st
import pymongo         # Our Python Driver to connect to MongoDB
import pandas as pd
import numpy as np
import os
import json
import re
from datetime import datetime
import datetime as dt
import string

from PIL import Image # For imaging support
import yahoo_fin.stock_info as si

# * ------------------------------------------------------------------------------- * #
class Company:

    """ For Displaying Financial Data in Dashboard  """

    def __init__(self, ticker):

        # * ----------------------------------------- * #
        """
        :param ticker: Ticker symbol and search keyboard
        """
        # * ----------------------------------------- * #
        price_df = si.get_data(ticker, dt.datetime.now() -

                dt.timedelta(days = 2 * 356),  # Delta out data for formatting

                dt.datetime.date(
                    dt.datetime.now()
        ))

        # Parameter to Overview Financial Data from APIs
        overview_df = si.get_stats(ticker)
        overview_df = overview_df.set_index("Attribute")
        overvie_dict = si.get_quote_table(ticker)

        income_statement = si.get_income_statement(ticker) # Income Statements
        balance_sheet = si.get_balance_sheet(ticker)       # Balance Sheet
        cash_flows = si.get_cash_flow(ticker)             # Cash Flows

        # Custom Inheritance Methods to manipulate above code
        self.year_end = overview_df.loc["Fiscal Year Ends"][0]

       # self.market_cap = get_integer(
       #     overview_dict["Market Cap"]
       # )

       # self.market_cap_cs = "{:,d}".format(
       #     int(self.market_cap)
       # )

        self.prices = price_df["adjclose"]

        self.sales = income_statement.loc["totalRevenue"][0]
        self.gross_profit = income_statement.loc["grossProfit"][0]
        self.ebit = income_statement.loc["ebit"][0]
        self.interest = - income_statement.loc["interestExpense"][0]
        self.net_profit = income_statement.loc['netIncome'][0]

    def get_overview(self):

        # * ----------------------------------- * #
        """
        :return:
        """
        # * ----------------------------------- * #
        self.price_earnings_ratio = self.market_cap / self.net_profit
        self.ev_sales_ratio = self.ev / self.sales

        self.overview_df = {

            "Values" : [
                self.ev_cs, self.market_cap_cs,
                    self.ev_sales_ratio,
                        self.price_earnings_ratio
            ]
        }

    def get_profit_margins(self):

        # * -------------------------------- * #
        """
        :return:
        """
        # * -------------------------------- * #
        self.gross_margin = self.gross_profit / self.sales
        self.operating_margin = self.ebit /self.sales
        self.net_margin = self.net_profit / self.sales

        self.profit_margin_dict = {
            self.gross_margin, self.operating_margin,
            self.net_margin
        }


# * ------------------------------------------------------------------------------- * #
def main():

    # * ------------------------------------------- * #
    """
          Just wrap prodecual code into a wrapper function for event calling
    """
    # * ------------------------------------------- * #
    st.title("Firenance! Network")  # Give the interface a title
    st.write(
        """
        ## Dashboard Interface
        
        """)

    user_input = st.text_input(
        "Enter Cryptocurrency ot Ticker Index Symbol"
    )

    search_button = st.button("Search")

    if search_button:

        company = Company(user_input)
        company.get_overview()
        company.get_profit_margins()

        overview_index = [
            "Enterprise Value", "Market Cap",
            "EV/Sales Ratio",
            "P/E Ratio"
        ]

        overview_df = pd.DataFrame(
            company.overview_dict,
                 index = overview_index
        )

        st.line_chart(company.prices)
        st.table(overview_df)

        with st.beta_expander(
            "Profit Margins (as of {}".format(
                company.year_end)):

            profit_margin_index = [
                "Gross Margin",
                "Operating Margin",
                "Net Margin"
            ]

            profit_margin_df = pd.DataFrame(
                company.profit_margin_dict,
                    index = profit_margin_index
            )

            st.table(profit_margin_df)
            st.bar_chart(profit_margin_df)


    # Content for widgets
    #with st.form(key = "my_form"):

     #   user_name = st.text_input(
     #       label = "Enter Cryptocurrency or Ticker Symbol"
     #   )

        # The submit button to initiate Fireadmin command in this context
    #    submit_button = st.form_submit_button(
     #       label = "Search"
     #   )

    # Here we make a sidebar to access Firenance chainanalysis
    # st.header("Firefly!")

    variable_str_SelBox = st.header("Firefly! Ecosystem of Apps & dApps")

    # * ----------------------------------------------------------- * #
    # FireflyAdmin App Sidebar in Streamlit UX & Firestreams other platforms
    # * ----------------------------------------------------------- * #

    # toDO --> Need to build in Naturual Language AI-Sentiment Analyzer.
    #          Here is where I want OpenAI to provide NL Sentiment to users
    #          using the Firestream Interace to interact with Firenance Network,
    #          using either a Firefly! App or a Firefly! dApp

    st.sidebar.title("Firenance! Network Firestream Interface")


    # Checkbox to start teh conditional Navigations for Admin
    # This will at first hide teh checkbox, you to deselect the check box
    # To connect Firestream on Firenaet, using FireCrypt! Protocol
    # * ---------------------------------------------------------- * #

    if not st.sidebar.checkbox(
            "Firestream Interface", True,
            key = "1"
    ):
        col1, col2, col3 = st.columns(3)

        with col2:
            st.image("images/fire.png")

        st.title("Firenance! DeFi-Blockchain")

        # If the Admin Selects Firecoin! Digital Coin Firestream

        coin_selected = st.sidebar.selectbox(

            "Select a Digital Coin of Firenet & FireCrypt Protocol",

            (
                "Firecoin!",  # Chronogical Cryptocurrency
                "Firetoken!", # Arbitary & Liquidity Crypto Memetoken
                "FireTON!"
            ))   # TON-Fungible Stablecoin & "Microtoken"


        # * ------------------------------------ # #
        # If the Admin Selects Firecoin! Digital Coin Firestream
        if coin_selected == "Firecoin!":

            # Bring the Price of Firecoin! on Firenance! Network
            st.write(
                """
                ## Firecoin! Connecting to Firenance! Network...
                
                This is the Ecosystem's Chronical and Pivitol Cryptocurreny.
                It works as ar Ring or "Pure" Proof-of-Work on Block-Produced Smart Contracts
                of Firenance! Network, Firefly!' DeFi-Blockchain and Crypto Exchange. We graphically
                use 'firestreams'. Which make use of Threaded Network Fibres across varies
                other blockchain ecosystems, via an exchangle and fungible means. This is a Byzannite
                Asset and only has finite supply, through its consenses & life. There is a supply
                of 52,500,000 Firecoins, exactly two and a half that of Bitcoin. 
                Fire! pay homage to the Bit in M-Theory for this reason. This is sacred, and is blasphemic 
                if altered. Firecoin! is mathematcally based on the 'micro-calculus'. a branch of 
                calculi, attempting to forge String Theory into Two main theories, instead of Five.
                We use the mathematical of Super Symmetry, instead of Chronic Symmetry or Assemetry. 
                """
            )

            # Put FireCrypt! Logo in SIdebar
            st.sidebar.image("images/firecoin.jpg")

            # Give brief laments explain, on how FireCrypt Protocol is build
            st.sidebar.write(
                """
                ## Firecoin! is a 'Ringed' Proof-of-Work (rPoW) Cryptocurrency.
                
                Its computation, is that of a Byzannite Asset, who's data is spread over
                a peer-to-peer network, using a "bubbling meme" as a data structure. We build 
                a block on top of a Web Socket, and feed them into a chain. Using a Merkle-Tree, as a
                Data Stucture, we build a Chain of interloping blocks, and use a decentralized 
                network of interconnected computers, as nodes to distribute the data into 
                a digital ledger, without the requirement of third party services. This digital ledger
                is public, however obscurely random, and not readable by humans, only machines.
                
                """
            )


            st.metric(
                label = "Firecoin! (Firenance! Network)",
                value = "$0.0000000001",
                delta = "+0.50% ⬆ 📈️"
            )

        elif coin_selected == "Firetoken!":

            # Bring the Price of Firetoken! on Firefly App & dApp EcocSys

            st.write(
                """
                ## Firetoken! Connecting to Firefly! Cloud...
                 
                This is the Ecosystem's Arbitary & Liquidity Crypto Memetoken.
                Firetokens!' are arbitary, and therefore, there is an infinite supply of them.
                It operates as a cryptocurrency, using a 'Progressive' Paradigm of Scrypt Encryption, making 'inhouse-tokens'
                to work on the FireCloud! Bot-API Platform & Firenance! Network, these are only 
                exchangable within the Firefly! Cloud & Firenance! DeFi-Blockchain Network.
                """
            )

            # Put FireCrypt! Logo in SIdebar
            st.sidebar.image("images/firetoken.jpg")

            # Description of Firetoken!
            st.sidebar.write(
                """
                ## Firetoken! is Peer-to-Peer Cryptocurrency, based on 'Progressive' Proof-of-Work
                PPoW (aS it may be).
                It is based on the pheonomena of the 'memecoin', similar to Dogecoin, Shiba-Inu,
                & Safemoon. It is an extremely volatile digital coin, and this is by
                design. Intended to keep the 8-cell Hyper-Routecubing of Blocks, "bubbling", and in 
                the paradigm of a Meme. 
                
                
                
                """
            )

            st.metric(
                label = "Firetoken! (FireCloud! Platform & Firenance! Network)",
                value = "-$0.00000000001",
                delta = "-0.50% ⬇️📉 "
            )



            # toDO --> build button widget to mine chain

        elif coin_selected == "FireTON!":

            # Bring Firefly!' Micro-Social App Microtoken from TON & Telegram
            st.write(
                """
                ## FireTON! Connecting to Telegram Cloud Platfom & TON Blockchain
                
                This makes the Ecosystem's 'Microtoken' and TON-based fungible Stablecoin.
                FireTON! is a type of Stablecoin whereby it acts as a 'reward-token' on the Telegram
                Payments API & Platform & The Open Network. It is regulated through its consensus,
                using TON's Proof-of-Stake (PoS), It is a 'Micro-Social' App of the Firefly!
                Ecosystem of Apps & dApps, bridging the Telegram Cloud Platfom, TON-Blockchain 
                through 'firestreams' of threaded network fibres to Firenance! Network & the FireCrypt
                DeFi-Blockchain. 
                """
            )

            # Put the FireTON Stablecoin Logo in SideBar
            st.sidebar.image("images/FireTON.jpg")

            st.metric(
                label = "FireTON! (Telegram App & The Open Network)",
                value = "$0.00000000",
                delta = "0.00% 💳 ✔️"
            )

        else:

            # toDo --> Put Firecoins Overall Fsinancial Metrics here
            st.image("images/fire.png")



# * --------------------------------------------------------------------- * #

# * $ * ====================================================== * $ *
if __name__ == "__main__":
    main()
# * $ * ====================================================== * $ *



# * -------------------------------------------------------------------------- * #
"""
          * Ok, so right now this is rather very basic and simple, but from here
            We start building what the Firenance!' "Open Ledger" will do in the context
            of Peet-to-Peer cryptographic transactions, of Firecoin! & Firetoken! over Firenance!
            DeFi Network itself.

          * This script will not facilitate "Micro-Social" App or dApp cryptocurrecies,
            falling under the Project's 8-cell Hypercube Cryptosysytem. FireCrypt! Protocol,
            is not a multichain ecosystem, rather a technological inversion of it.

          * We attempt this concept so that it work can flawlessly on other Multichain
            Ecosystems, like Polkadot, Algorand, TON, etc... As well as a normal Web2.0 Application
            to form a bridge to coming Web3.0 and Blockchain Metaverse. (The two will be slighty
            diffirent in computational UX.)

          * These bridges, are efficient cross chain Oracles I like to call "firestreams",
            and I kinda envision they work the same as calculi, giving the axiom to make
            all types of reflections occur, in the updated context & objectivity of Human Reality.


"""
# * -------------------------------------------------------------------------- * #

import pyfiglet   # So terminal looks pretty for troubleshooters
from colorama import Fore, Back, Style  # For different color for terminal and logger out
from ring_fire import HyperBlock, HyperBlockchain

def transaction_1():

    # * -------------------------------------- * #
    """

          This is a very basic mining instance on
          Firenance!, which will accept FireCrypt! Protocol
          to define the HyperBlockchain "Open" Ledger. This will be hosted
          on dencentralized noded network of computers, or "miners"

          Everyone will be able to see transaction, just not see the readable
          context of it. Only machines can understand the information,
          using the defined Election Scheme, and Distributed Trust System.

          Should anything be comspicuous, perhaps illict happening when
          a block is being mined, Firecrypt will send the meta data of the transactions
          to an AI-enabled "honey-pot", for security analysis and tokenized research.

          This will shutdown the entire consensus, and this will be the only time
          the Merkle Tree Data Structure will fork itself into a testnet. All wallets,
          will then be transfered in a cold vault system, offline from the Web.

    """

    # * ---------------------------------------------------------------- * #
    """ 
         Call the script that defines the HyperBlockchain, and cryptographic
         instances of Firecoin! & Firetoken!, hashing over Firenance Network!
         
         Here we build the UX and frontend of it all, which I would like to 
         use Strealit Web Framework, this is perhaps only for now, and maybe
         Django would be a better Web Framework to use. I I must properly
         learn how to use that! 
    """
    # * ---------------------------------------------------------------- * #

    blockchain = HyperBlockchain() # Call the HyperBlockchain Script in Fron End UX

    # * ----------------------------------------------------------------- * #
    #     Play Graphics, to give scalar context for future
    #     Front End development..
    # * ----------------------------------------------------------------- * #
    header_logger = pyfiglet.figlet_format("Firenance! Network")
    footer_for_logger = pyfiglet.figlet_format("FireWallet!")

    print(Fore.RED + header_logger) # Just to show a UX Header of Open Legder
    print("")
    print("$ * ============================================== * $")
    print("")
    print(Fore.CYAN + " Firenance! Network Open Ledger: \n")
    print(Fore.BLUE + str(blockchain.chain))
    print("")
    print("$ * ============================================== * $")
    print(Fore.CYAN + footer_for_logger)
    print("")

    # Methodology to embed backend into Front End UX
    last_block = blockchain.last_block  # Get the last block of "rotating" chain
    last_proof_no = last_block.proof_no # Get the rPoW of last activate HyperBlock
    proof_no = blockchain.proof_of_work(last_proof_no) # toDO --> Hashing must adapt to RingCTs

    get_amount = input("Quantity of Transfer?: ")

    # * ----------------------------------------------------------------- * #
    #                      END of UX Front End Section
    # * ----------------------------------------------------------------- * #

    # * ----------------------------------------------------------------- * #
    #   Mining instances of a Firenance! Transaction, IE; Validation for Transaction
    #   & the actual transaction to occur and be added to the HyperBlockchain.
    #   Valdation is dependant to FireCrypt! Encryption to give "rPoW"...
    # * ---------------------------------------------------------------- * #

    # Offer new data to HyperBlockchain for rPoW Validation.
    blockchain.new_data(
        sender = "0",
        recipient = "SeanCode",
        quantity = get_amount,
    )

    # This is calling FireCrypt! Encryption to give validility for
    # p2p transaction to occur over the Firenance! Network....
    last_hash = last_block.calculate_hash  # toDO --> This is where our Ring Signatures will go

    # If FireCrypt! validates, form a "hyperblock"
    hyper_block = blockchain.construct_block(
        proof_no,
            last_hash
    )

    print("")
    print(Fore.BLUE + "***Mining has been Successful!!***")
    print("")
    print(Fore.CYAN + str(blockchain.chain)) # Make ammend into HyperBlockchain

def transaction_2():

    # * ------------------------------------ * #
    """
    :return:
    """
    # * ------------------------------------ * #



if __name__ == '__main__':
    transaction_1()




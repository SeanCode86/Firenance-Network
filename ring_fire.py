# * ------------------------------------------------------------------------------------------- * #
"""
                                 Firecoin! Cryptocurrency
                                           &
                                   Firenance! Network
                                       Blockchain

                                                            by SeanCode

     This script is the actual backbone of the entire Blockchain. The skeleton of it if you wanna
     call it that. This will build the Merkle Tree data structure of what we use to chain our
     Block-Produced Smart Contracts. So in essense this really how Firenance! will be a decentralized
     Network. The combination of this, RingCT Encryption Signatures from Monero, and the Fourier Series
     Sets and inline function for Firecoin!' memetoken; Firetoken! will form the initial basis
     for FireCrypt Encryption Protocol, or so I hope! LoL

     The idea behind Firecoin! is to build what i like to call a "rPoW" Algorithmic consensus.
     Firecoin! is a Privacy-focused Digital Coin, inspired by the Monero DC. Though we use
     other elements and mathematcial concepts from Algorand Ecosystem and the TON-BLockchain. I also
     was inspired by how Shiba-Inu Ecosystem was buitl, whereby it has three cryptocurrenci to the
     it, perhaps I was still pretyy ignorant at the time, but I the idea of incorporating
     the Trinity into it, menaing it will three different types of Digital Coins to facilitate
     one Blockchain, where it is a Distributed System of Trust, a Blockchain Election scheme, and
     Cryptography created by ALFA Research Group, where I use RingCT Encryption to hash transactional
     block.

"""
# * ------------------------------------------------------------------------------------------- * #
# Our Imports
import socket    # We build blocks of the chain from web sockets in Python

# For BLock Produce Firecoin! & Programmable Financial Asset
import hashlib  # For Hashing Algorithm SHA-256
import time     # For Block timestamp and to help with threading

# For RingCT Signatures (Adopted from Monero Cryptocurrency)
# RingCTs are used used to obscrube numeric digits, representing the value of a transaction,
# So we must import our external scripts, that utilize RingCT Module. We import our
# scripts from /src directory with the Python Virtual Environment

# import src.ringCT_encrypt as rEncrypto_inferno  # toDO --> Ok I have made this script yet...
# import secrets

# * ------------------------------------------------------------------------------------------- * #

class HyperBlock:

    """
         Our Class defining how the socket we made in server scripts
         make client connect to server. Here we enable a user to mine
         and make use of Firecoin! This Socket, is a networking socket
         being presented to the server as a Block, of a Merkle Tree Data Structure
    """

    def __init__(
            self,
            #host = "localhost",
            #port = 55757, # toDO --> This must be derivative

            index = "",
            proof_no = "",
            prev_hash = "",
            data = "",
            timestamp = None):

        # * ------------------------------------------------------------------ * #
        """
        :param host:       The IP of the host we make the SocketBlock run on
        :param port:       The port it will bind to onto web server script
        :param index:      Index what block is chronologically what...
        :param proof_no:   Our Proof-of-Work, to make block valid to chain
        :param prev_hash:  The previous hash of that chained block
        :param data:       Data making up the digital transaction
        :param timestamp:  The timestamp entried in Merkle Tree Digital Legder
        """
        # * ----------------------------------------------------------------- & #

        # For networtivity, and make Socket a Block of Merkle tree
        #self.sock = socket.socket()

        #self.sock.connect(
        #    (host, port) # COnnect host to port and Go!
        #)

        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data

        # The timestamp for the block made onto Socket
        self.timestamp = time.time() # Define as its hashed...

    @property
    def calculate_hash(self):

        # * ---------------------------------- * #
        """
                This function will calculate the hash
                for every block made... Here we need to make
                a string of the data, so we can parse it
        """
        # * ---------------------------------- * #

        # Make format for block to be a string. . .
        block_string = "{}{}{}{}{}".format(
            self.index, self.proof_no,
            self.prev_hash, self.data,
            self.timestamp
        )

        # Apply Hashing algorithm and dump the shit man!
        # toDO --> We must use 3rd version of NSA SHA-256, like
        # RingCT are implemented with work done by ALFA Research Group,
        # & used in Monero Cryptocurrency to obscure digital values
        # used to determine the value of a Peer-to=Peer Transaction.
        # So no one can see how much money is being in it

        return hashlib.sha256(
            block_string.encode()).hexdigest() # --> toDO this must be sha256(3) algorithm.

    def __repr__(self):

        # * ------------------------------------ * #
        """

                After we initialize HAshing, just make
                this so that we may parse thing better...

        """
        # * ------------------------------------ * #
        return "{} - {} - {} - {} - {}".format(
            self.index, self.proof_no,
            self.prev_hash, self.data,
            self.timestamp
        )

   # def get_data(self):

        # * -------------------------------- * #
    #    """
    #    :return:  Get data from request and response
    #              The returns the data produced into Kivy Widget
    #              Instance...
    #    """
     #   # * -------------------------------- * #
      #  return self.sock.recv(1024)

# * ---------------------------------------------------------------------------------- * #
"""
                 The ACTUAL BLOCKCHAIN defining Merkle Tree Data Structure
                 for Firecoin! Privacy Digital Coin. This is the chronical coin
                 of the Firenance! Network, and the FireCrypt Encyption Protocol
"""
# * ---------------------------------------------------------------------------------- * #

class HyperBlockchain:

    def __init__(self):

        # * -------------------------------- * #
        """
               The constructor method, feeding Block above
               into chain
        """
        # * -------------------------------- * #
        self.chain = []          # Chain is empty before genesis block
        self.current_data = []   # this keeps all completed transactions in block
        self.nodes = set()
        self.construct_genesis() # This will take care of building initial block

    # Now we must build a function to make a genesis block
    def construct_genesis(self):

        # $*$ ========================================= $*$ #
        """
        :return:     Firecoin! GENESIS_BLOCK() !!
        """
        # $*$ ========================================= $*$ #

        # Make counter for garbage collection..
        self.construct_block(
            proof_no = 0,
            prev_hash = 0
        ) # Reference Genesis Block to nullset value

    # To make A GENESIS BLOCK, the script needs to know what a SocketBlock is!
    def construct_block(
            self,
            proof_no = "",
            prev_hash = ""):

        # * ------------------------------------- * #
        """
        :param proof_no:   The SocketBlock to check defined by index
        :param prev_hash:  The prev_hash of block on Merkle Tree DS
        :return:           Create validility, and Proof-of-Work Consensus
        """
        # * ------------------------------------- * #

        # Build our Block, inheriting data from Parent Class
        # This parent class is what are the blocks which chain together
        # and struncure themselves like Merkle Trees

        # toDO --> I must make my signing function a Fourier Series
        #          within this function......

        # Yes to achieve the "whip", so
        # it corresponding with my "Special RelayRelativity" Theory.
        # for String Theory in Particle Physics.

        block = HyperBlock(

            index = len(self.chain),
            proof_no = proof_no,
            prev_hash = prev_hash,
            data = self.current_data
        )

        self.current_data = []    # What we store our block in
        self.chain.append(block)  # add or append new block and chain it to Merkle Tree

        return block

    @staticmethod
    def check_vadility(block, prev_block):

        # * ------------------------------ * #
        """
        :param block:        Thew block to check, defined by index
        :param prev_block:   The prev_block to chain to Merkle Tree
        :return:             Check validility and create Proof-of-Work
        """
        # * ------------------------------ * #

        # Our conditional we code to check the valdility

        # If the next hash is index wrong...
        if prev_block.index + 1 != block.prev_hash:
            return False

        # If this hash isnt the same as last in chain
        elif prev_block.calculate_hash != block.prev_hash:
            return False

        #
        elif not Blockchain.verifying_proof(
                block.proof_no, prev_block.proof_no):

            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True # If there are no errors after checking this return Chain

    def new_data(self, sender, recipient, quantity):

        # * --------------------------------- * #
        """
        :param sender:
        :param recipient:
        :param quantity:
        :return:
        """
        # * --------------------------------- * #
        self.current_data.append({
            "sender": sender,
            "recipient": recipient,
            "quantity": quantity
        })

        return True

    @staticmethod
    def proof_of_work(last_proof):

        # * ----------------------------- * #
        """
        This simple algorithm identifies a number f' such that hash(ff')
        contain 4 leading zeroes (We ammend a RingCT Signature), to invertedly hash
        the last zeros of f-hash is the previous f' f' will be the new proof

        :param last_proof:  The Proof-of-Work of previous block in chain,
                            we attempt to hash the tailing zeros with RIngCT
        :return:
        """
        # * ----------------------------- * #
        proof_no = 0    # Garbage Collection & Contextal Mutable Variable

        while HyperBlockchain.verification_proof(
                proof_no, last_proof   # The new proof request, must be the same as last block in chain
        ) is False:

            proof_no += 1  # If proof-of-work computated by chain, join block to it

        return proof_no    # Add a new entry into digital ledger

    @staticmethod
    def verification_proof(last_proof, proof):

        # * -------------------------------------- * #
        """

             Here we verify the proof of hash is there
             are four leading zeros. Firecoin!' get it unquie encryption
             which be probably a Ring fungilbe token or sorts (I think..)



        :param last_proof: The last block must contain the same RingCT Signature, like Monero
        :param proof:      Use SHA-256 Algorithm to hash block (for now).
                           Idea is to incorporate RingCT called from calculate_hash()
        :return:
        """
        # * -------------------------------------- * #

        tailing_zeros = "0000"

        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest() # --> toDo (RingCTs)
        return guess_hash[:4] == f"{tailing_zeros}"

        # toDO --> RingCT called from calculate_hash() function..



    @property
    def last_block(self):

        # * ------------------------------ * #
        """
             Return the last block from the chain
        """
        # * ------------------------------ * #
        return self.chain[-1]  # Bring data context "back-forward.."

    # * -------------------------------------------------------------------------------- * #
    """
              This is like the other main binary operator of what it takes
              to complete our little digital coin. Here make the Blockchain
              minable, so that transaction can be validated using the cryptocurrency.
              Thios is where nodes of our Merkle tree data strutcure get added
              by miner and makes a network of chained blocks
    """
    # * -------------------------------------------------------------------------------- * #
    # todo --> Here I have connect this to Flask Web framework. So I need to define routed
    #          decorator, so that the code can do HTTP resquests, and so that I make build
    #          an API
    # * -------------------------------------------------------------------------------- * #

    def block_minning(self, details_miner):

        # * -------------------------------------- * #
        """

        :param details_miner:  Details of machine mining and validateing transactions
                               or Block-Produced Smart Contract
        :return:               Start mining sequence to validated transaction into the chain
        """
        # * -------------------------------------- * #

        # Create node, which is made from corresponding indexed block
        self.new_data(
            sender = "0",
            reciever = details_miner,
            quantity = 1, # Creating new block (identify proof_no) award 1
        )

        last_block = self.latest_block     # The last block to proof-of-work consensus
        last_proof_no = last_block.proof_no # The last block, before the new transaction (same)
        proof_no = self.proof_of_work(last_proof_no) # And TaDa!!

        # Make it happen...

        last_hash = last_block.calculate_hash

        block = self.construct_block(
            proof_no,
            last_hash
        )

        return vars(block)

    def create_node(self, address):

        # * ----------------------------------- * #
        """

        :param address:  Here we need address of Wallet to make node
        :return:
        """
        # * ----------------------------------- * #
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):

        # * --------------------------------- * #
        """

        :param block_data:
        :return:
        """
        # * --------------------------------- * #

        return Block(
            block_data["index"],
            block_data["proof_no"],
            block_data["prev_hash"],
            block_data["data"],
            timestamp =["timestamp"]
        )

    # * -------------------------------------------------------------------------------- * #
    """                                   END !!
    """
    # * -------------------------------------------------------------------------------- * #












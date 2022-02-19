# * =========================================================================== * #
"""
       Elliptical Curve Script to hash a secp-256-k1 algorithm along a Merkle Tree
       data structure to produced a blockchain, which can be defined as it 'Open'
       Digital Ledger. This is intended for me to test Botcoin! with my Crypto
       Bot on Telegram, whereby I try make the consensus of a cryptocurrency work
       within the paradigm of a chat service like Telegram, Discord or WhatsApp.

       This script is the same as Bitcoin's cryptography, except I attempt to
       make it behave as a "Micro-Smartchain", prodducing "Block-Produced" Smart
       Contracts. Still in its very infancy, as I am using this as a way to better
       understand the cryptography defined by US FED's SHS Handbook for Hashing
       SHA Algorithms. This is SHA-256 secp-k1 written in Python instead of C++,
       and written without any dependendancies. So this will take a while to get
       right, well what's in my head about it anyway!

                                                            --> SeanCode👽
"""
# * =========================================================================== * #

from __future__ import annotations
from dataclasses import dataclass
import time  # For asynchronous help for Memory Management

import pyfiglet   # So terminal looks pretty for troubleshooters
from colorama import Fore, Back, Style  # For different color for terminal and logger out

# * ========================================================================== * #
@dataclass
class Curve:

    # * ----------------------------------------------- * #
    """
        Elliptical Curve over the field of integers modulo
        a prime.

        Points on the curve statisfy y^2 = x^3 + a*x + b (mod p)
    """
    # * ----------------------------------------------- * #

    p: int  # The Prime Modulus of the Finite Field
    a: int  # First point of Curve
    b: int  # Second Point of Curve

    # Just as an example to better understand ECC, lets use curve defined by secp256k1
    # This is what Bitcoin uses, I adapt this to ECCs used in Monero later on...
    # Bitcoin uses 'secp256k1', whereby a = 0 and b = 7, making ECC y^2 = x^3 + 7 (mod p)

bitcoin_curve = Curve(
        p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
        a = 0x0000000000000000000000000000000000000000000000000000000000000000, # a = 0
        b = 0x0000000000000000000000000000000000000000000000000000000000000007, # b = 7
    )

# * ========================================================================== * #
@dataclass
class Point:

    # * --------------------------------------------- * #
    """
         Here we define as a class, what's know as an ECC's Generator Point
         Which is a like the starting point to whole cycle of the Elliptical Curve
    """
    # * --------------------------------------------- * #

    curve: Curve
    x: int
    y: int

G = Point(
        bitcoin_curve, # Use the ECC defined in Curve class
        x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
    )

# * ========================================================================== * #
""" 
    Now we know where on the curve we have placed the generation point. This is
    like an instance when a proof-of-concept comes into sight, in Firecoin! lingo
    I call it a "proof-to-occur". All this is placing the metadata of what the curve 
    will and we place such information in its own class. This will also generate the
    private access key, created by the hashing encryption, we define from this class,
    in this case it it curve; "secp256k1", which is an SHA-256 Algororithm, used in Bitcoin.
    The shaped curve or "size of the set", and one used to create a private key, over 
    a public domain. 
"""

# * ========================================================================== * #
@dataclass
class Generator:

    """
        A generator point going, over the curve defined.
        A initial point the pre-computed order to things
        henve "proof-of-concept" or a "proof-to-occur"
    """

    G: Point # A generator point on the curve
    n: int   # The order of generating point, so; 0*G = n*G = INF

bitcoin_gen = Generator(
    G = G,
    # the order of G is known and can be mathematically derived
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
)

# * ========================================================================== * #
"""
     Here we are going to generate the public key. The Public Key, is the point
     on the curve, which results from adding the generator point to itself,
     secret_key times. Hence;
     
         public_key = G + G + (secret_key times) + G = secret_key * G 
"""
# * ========================================================================== * #
INF = Point(None, None, None) # Special point at "Infinity", kinda like what a zero is

def extended_euclidean_algorithm(a, b):

    # * -------------------------------------- * #
    """
    :param a:  First point
    :param b:  Second Point

    :return:  (gcd, x, y) s.t. a * x + b * y === gcd
              This function implements the extended Euclidean
              Algorithm and run in 0(log b) in worst case...
    """
    # * -------------------------------------- * #

    # Build our Binary Operators to move in
    # Logarithms, along the SECP256k1 Elliptical Curve

    old_r, r = a, b  # Our binary operators, to create tuple
    old_s, s = 1, 0  # Integizing one way for PoC
    old_t, t = 0, 1  # Integizing other wat for Vefified PoW

    while r != 0:    # While r is moving as a logarithm over ECC do this. . .

        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t # "SPin" the Communtative Rings into Mathematical Closure

# * ---------------------------------------------------------- * #

def inv(n, p):

    # * ------------------------------------- * #
    """
    :param n:  The point we defined as Generator inside secp256k1 Algorithm
    :param p:  The point to go in Infinity or Elliptical Curve SHA256k1
    :return:   Modular multiplication inverse m s.t. (n * m) % p == 1
    """
    # * ------------------------------------- * #
    gcd, x, y = extended_euclidean_algorithm(n, p)
    return x % p # Let it return back and make Communtation for next point

# * ---------------------------------------------------------- * #

def elliptic_curve_addition(self,
                            other: Point) -> Point:

    # * ------------------------------------ * #
    """
    :param self:   Some point as ANon
    :param other:  Generator Point of Elliptical Curve
    :return:       This adds on another logarithm usimg extended Euclidean Algorithm
    """
    # * ------------------------------------ * #

    # Handle special case of P + 0 = 0 + P = 0
    if self == INF:
        return other
    if other == INF:
        return self

    # Handle Special Case of P + (-P) = 0
    if self.x == other.x and self.y != other.y:
        return INF

    # Compute the slope
    if self.x == other.x: #(self.y = other.y is guaranteed too per above check)
        m = (3 * self.x ** 2 + self.curve.a) * \
            inv(2 * self.y, self.curve.p
    )

    else:
        m = (self.y - other.y) * \
            inv(self.x - other.x, self.curve.p
        )

    # Now we compute new Point
    rx = (m ** 2 - self.x - other.x) % self.curve.p
    ry = (-(m * (rx - self.x) + self.y)) % self.curve.p
    return Point(self.curve, rx, ry)

# * ---------------------------------------------------------- * #

def double_and_add(self, k: int) -> Point:

    # * ------------------------------------- * #
    """
    :param self: Logarthm, follwing Curve
    :param k:    The Generator Point of ECC secp256k1
    :return:     This is like facilitates the shifting of
                 the algorithm over the curve
    """
    # * ------------------------------------- * #

    assert isinstance(k, int) and k >= 0
    result = INF    # All ECCs must a point, whereby we give a reference for Infinity
    append = self

    while k:
        if k & 1:
            result += append
        append += append

        k >>= 1

    return result

# * ---------------------------------------------------------- * #
""" 
    After all that we have created a cryptographic identity, which 
    can be used to create hash functions, using our ECC algorithm
"""
# * ---------------------------------------------------------- * #

def gen_sha256_with_variable_scope_protector_to_not_pollute_global_namespace():

    # * ----------------------------------------------- * #
    """
    SHA256 implementation.

    Follows the FIPS PUB 180-4 description for calculating SHA-256 hash function
    https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf

    No one in their right mind should use this for any serious reason. This was written
    purely for educational purposes.
    """
    # * ----------------------------------------------- * #

    import math
    from itertools import count, islice

    # * # -------------------------------------------- # * #
    #                  INLINE FUNCTIONS()
    # * # -------------------------------------------- # * #
    #              SHA-256 Functions, defined in
    #              Section 4 of FIPS PUB 180-4
    #              Secure Standard Hash Standard (SHS)
    # * # --------------------------------------------- # * #

    def rotr(x, n, size = 32):

        # * --------- * --------- * #
        """
        :param x:    Our generator point on ECC
        :param n:    The order of GP defined from Bitcoin's GP of secp256k1
        :param size: Size of the Rotation

        :return:     Return teh digital representation of the rotor size
        """
        # * --------- * --------- * #
        return (x >> n | (x << size - n) &
                    (2 ** size - 1)
        )
        # * --------- * --------- * #

    # * # ------------------------------------- # * #
    def shr(x, n):

        # * --------- * --------- * #
        """
        :param x:  Generator Point of ECC
        :param n:  Order Point from bitcoin_gen()
        :return:   Right SHift Bitwise Operation
        """
        # * --------- * --------- * #
        return x >> n
        # * --------- * --------- * #

    # * # ------------------------------------- # * #
    def sig0(x):

        # * --------- * --------- * #
        """
        :param x: Generator Point of ECC
        :return:  Rotor shift right Bitwise
                  on point x
        """
        # * --------- * --------- * #
        return rotr(
            x, 7) ^ rotr(x, 18) \
                  ^ shr(x, 3
        )
        # * --------- * --------- * #

    # * # ------------------------------------- # * #
    def sig1(x):

        # * --------- * --------- * #
        """
        :param x:
        :return:
        """
        # * --------- * --------- * #
        return rotr(
            x, 17) ^ rotr(x, 19) \
               ^ shr(x, 10
        )
        # * --------- * --------- * #

    # * # ------------------------------------- # * #q
    def capsig0(x):

        # * --------- * --------- * #
        """
        :param x:
        :return:
        """
        # * --------- * --------- * #
        return rotr(
            (x, 2) ^
            rotr(x, 13) ^ rotr(x, 22)
        )
        # * --------- * --------- * #

    # * # ------------------------------------- # * #
    def capsig1(x):

        # --------- * --------- * #
        """
        :param x:
        :return:
        """
        # --------- * --------- * #
        return rotr(
            (x, 6) ^
            rotr(x, 11) ^ rotr(x, 25)
        )
        # --------- * --------- * #

    # * # ------------------------------------- # * #
    def ch(x, y, z):

        # --------- * --------- * #
        """
        :param x:
        :param y:
        :param z:
        :return:
        """
        # --------- * --------- * #
        return (x & y) ^ (~x & z)
        # --------- * --------- * #

    # * # ------------------------------------- # * #
    def maj(x, y, z):

        # --------- * --------- * #
        """
        :param x:
        :param y:
        :param z:
        :return:
        """
        # --------- * --------- * #
        return (x & y) ^ \
               (x & z) ^ (y & z)
        # --------- * --------- * #

    # * # ------------------------------------- # * #
    def b2i(b):

        # --------- * --------- * #
        """
        :param b:
        :return:
        """
        # --------- * --------- * #
        return int.from_bytes(b, "big")
        # --------- * --------- * #

    # * # ------------------------------------- # * #
    def i2b(i):

        # --------- * --------- * #
        """
        :param i:
        :return:
        """
        # --------- * --------- * #
        return i.to_bytes(4, "big")
        # --------- * --------- * #

    # * ------------------------------------------ * #
    #                             SHA Constants
    # * ------------------------------------------ * #
    def is_prime(n):

        # * --------- * --------- * #
        """
        :param n:  Generator Point or ECC ID Element of SECP356k1
        :return:
        """
        # * --------- * --------- #
        return not any(

            f for f in range(
                2, int(math.sqrt(n)) + 1)
            if n % f == 0
        )
        # * --------- * --------- #

    # * ------------------------------------- * #
    def first_n_primes(n):

        # * --------- * --------- #
        """
        :param n:
        :return:
        """
        # * --------- * -------- * #
        return islice(

            filter(
                is_prime,
                count(start = 2)
            ), n
        )
        # * ------------------------- * #

    # * -------------------------------------- * #
    def frac_bin(f, n = 32):

        # * --------- * --------- * #
        """
        :param f:
        :param n:
        :return:   Return teh first n bits of fractional part of float
        """
        # * --------- * --------- * #
        f = math.floor(f)    # Get only the fractional part
        f *= 2 ** n          # Shift it left
        f = int(f)           # Truncate the rest of the fractional content

        return f
        # * ---------- * ----------- * #

    # * ------------------------------------- * #
    def genK():

        # * --------- * --------- * #
        """
        :return:  Follows Section 4.2.2 to generate K

            The first 32 bits of the fractional parts of the cube roots of the first
            64 prime numbers:

            428a2f98 71374491 b5c0fbcf e9b5dba5 3956c25b 59f111f1 923f82a4 ab1c5ed5
            d807aa98 12835b01 243185be 550c7dc3 72be5d74 80deb1fe 9bdc06a7 c19bf174
            e49b69c1 efbe4786 0fc19dc6 240ca1cc 2de92c6f 4a7484aa 5cb0a9dc 76f988da
            983e5152 a831c66d b00327c8 bf597fc7 c6e00bf3 d5a79147 06ca6351 14292967
            27b70a85 2e1b2138 4d2c6dfc 53380d13 650a7354 766a0abb 81c2c92e 92722c85
            a2bfe8a1 a81a664b c24b8b70 c76c51a3 d192e819 d6990624 f40e3585 106aa070
            19a4c116 1e376c08 2748774c 34b0bcb5 391c0cb3 4ed8aa4a 5b9cca4f 682e6ff3
            748f82ee 78a5636f 84c87814 8cc70208 90befffa a4506ceb bef9a3f7 c67178f2
        """
        # * --------- * --------- * #

        return [frac_bin(p ** (1/3.0))
                for p in first_n_primes(64)
        ]
        # * ---------- * --------- #

    # * ----------------------------------- * #
    def genH():

        # * --------- * --------- * #
        """
        :return:   Follows Section 5.3.3 to generate the initial hash value H^0

            The first 32 bits of the fractional parts of the square roots of
            the first 8 prime numbers.

            6a09e667 bb67ae85 3c6ef372 a54ff53a 9b05688c 510e527f 1f83d9ab 5be0cd19
        """
        # * --------- * ---------- * #

        return [frac_bin(p ** (1/2.0))
                for p in first_n_primes(8)
        ]

    # * -------------------------------------------------------------------- * #
    def pad(b):
        
        # * --------- * --------- #
        """
                   This is something known as padding
        :param b: 
        :return: 
        """
        # * --------- * --------- #
        b = bytearray(b) # Convert to mutable equivalent
        l = len(b)       # This will return the number of bytes and not bits
        
        # Append but "1" to the end of the message
        b.append(0b10000000) # Appending 10000000 in binary (=128 in decimal)

        # Follow logarithms along k zero bits, where ki is the smallest non-negative
        # Solution to l + 1 + k == 448 mod 512
        # Zero pad Message with zeros until we reach 448 or our
        # modolus of 512 bits
        while (len(b) * 8) % 512 != 448:
            b.append(0x00)

        # The last 64-bit block is the length l of the orignal message
        # Expressed in Binary Code (Big ENdian). . .
        b.extend(l.to_bytes(8, "big"))

        return b
   
    # * -------------------------------------------------------------------- * #

    def sha256(b: bytes) -> bytes:

        # * ------------------------------- * #
        """
        :param b:
        :return:
        """
        # * ------------------------------- * #

        # Section 4.2 of SHS Handbook
        K = genK()

        # Section 5: Preprocessing
        # Section 5.1: Pad the message
        b = pad(b)

        # Section 5.2: Separate the message into blocks of 512 bits (64 bytes)
        blocks = [b[i: i + 64]
                  for i in range(0, len(b), 64)
        ]

        # For each message Block M^1 ... M^N
        H = genH() # Section 5.3 of SHS Handbook

        # Section 6 of SHS
        for M in blocks:    # EaCH BLOCK is 64-entry array of 512 bits (64 Bytes)

            # Prepare the message shedule, a 64-entry array of 32 bit words
            W = []

            for t in range(64):
                if t <= 15:
                    # The first 16 words are just a copy of the block
                    W.append(bytes(M[t * 4:t * 4 + 4]))

                else:
                    term1 = sig1(b2i(
                        W[t - 2]
                    ))

                    term2 = b2i(W[t - 7])

                    term3 = sig0(
                        b2i(W[t-15])
                    )

                    term4 = b2i(W[t-16])
                
                    total = (term1 +
                             term2 + term3 +
                                 term4) % 2**32
                
                    W.append(i2b(total))

            # Initialize the 8 working variables a, b, c, d, e, f, g, h with prev hash value
            a, b, c, d, e, f, g, h = H

            # 3.
            for t in range(64):

                # toDO -->> Seem to be having two data type forming
                #           and they are conflicting. . .

                T1 = (h + capsig1(e) + \
                      ch(e, f, g) + K[t] + \
                          b2i(W[t])
                ) % 2 ** 32

                T2 = (capsig0(a) +
                      maj(a, b, c)) % 2 ** 32

                h = g
                g = f
                f = e
                e = (d + T1) % 2 ** 32
                d = c
                b = a
                a = (T1 + T2) % 2 ** 32

            # 4. Compute the i-th intermediate hash value H^1
            delta = [a, b, c, d, e, f, g, h]

            H = [
                (i1 + i2) % 2 ** 32
                    for i1, i2 in zip(
                        H, delta)
        ]

        return b''.join(i2b(i) for i in H)

    return sha256


# * -------------------------------------------------------------------- * #
#   Verfication if Point are placed correctly, according to what we define
# * -------------------------------------------------------------------- * #

# Verify that the Generator Point is  indeed on the curve,
# IE; y^2 = x^3 + 7 (mod p)

def main():

    # * -------------------------------------- * #
    """
              Wrapper function()
    """
    # * -------------------------------------- * #

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    header_logger = pyfiglet.figlet_format(" ECC secp-256-k1 \n"
                                           "             Firetest!")

    footer_for_logger = pyfiglet.figlet_format("                   Botcoin!")

    genesis_header = pyfiglet.figlet_format("    Genesis Block")

    time.sleep(1.5)

    print(Fore.RED + header_logger) # Just to show a UX Header of Open Legder

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    print(Fore.CYAN +
          "Generator IS on the Curve():? ",
                (G.y ** 2 - G.x ** 3 - 7) %
                  bitcoin_curve.p == 0
    )

    # Check if some other random point is not on the curve, not likely
    import random
    random.seed(1337)
    x = random.randrange(0, bitcoin_curve.p) # "Check" x Point
    y = random.randrange(0, bitcoin_curve.p) # "Check" y Point

    time.sleep(1.5)
    print("Is there a Totally Random Point on the Curve?: ",
        (y ** 2 - x ** 3 - 7 %
           bitcoin_curve.p == 0))

    time.sleep(1.5)
    print("Generating Test for Private Key...")
    time.sleep(1.0)

    print("")

    pvt_key_verify_test_codex = pyfiglet.figlet_format(
         f"Success!!"
    )

    print(Fore.GREEN + pvt_key_verify_test_codex)

    #print("")

    # The secret key
    secret_key = int.from_bytes(
        b"Hello Botcoin's Curve :-)",
            "big"
    )

    assert 1 <= secret_key < bitcoin_gen.n
    time.sleep(1.5)
    print("")
    print("Test Private Key Generation: \n", secret_key)
    print("")


    # * --------------------------------------------------------- * #
    #   Make different logarithms to chain the different hashes according
    #   to the point on the Ellipical Curve "SECP256k1", so when sk = 1
    #   it will in turn also equal sk = G & @ point 2 sk = G + G, etc..
    # * --------------------------------------------------------- * #

    # Now add Generator Point to make Public Key
    Point.__add__ = elliptic_curve_addition
    Point.__rmul__ = double_and_add

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    # Define our points
    sk = 1
    pk = G # Our Generator point

    # Efficiently calculate Public-Key
    public_key = secret_key * G

    time.sleep(1.0)

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    print("")

    print(Fore.RED +
          f"Add Layer 2 Verification...")

    time.sleep(1.0)

    print(Fore.LIGHTBLACK_EX +
          f"Genesis Routing & Connecteing to Merkle Tree DB?: ",
          (G == 1 * G)
    )

    time.sleep(1.0)
    print("")

    # Confirm that two points are are connected in reference
    # Generating Point of ECC secp256k1 Algorithm

    print(Fore.LIGHTBLUE_EX + f" X Point: {public_key.x}\n"
                          f" Y Point: {public_key.y}"
    )

    time.sleep(1.0)
    print("")

    print(Fore.GREEN + "Verify Genesis: ",
            (public_key.y ** 2 - public_key.x ** 3 - 7) %
          bitcoin_curve.p == 0
    )


    time.sleep(1.0)

    print("")

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    print(Fore.LIGHTGREEN_EX + genesis_header)

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    time.sleep(1.0)

    print(Fore.LIGHTBLACK_EX + f" Secret Key: {sk}\n\n"
          f" Public Key : \n\n"
              f"{(pk.x, pk.y)} \n"
    )
    print("")

    time.sleep(3.0)

    # Verfication public key
    print(f" Verify that Public Key is on the Curve & \n "
          f"that Genesis Block-Produced Smart Contract is connected...",

          (public_key.y ** 2 - public_key.x ** 3 - 7) %
              bitcoin_curve.p == 0
    )


    # If a second transaction comes along then public key must chain
    # IE; if indexing is 2 the G + G, aka, our "chain"...

    openLedger_graphic = pyfiglet.figlet_format("                 B l o c k   1 \n")

    print("")

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    print(Fore.LIGHTBLUE_EX + openLedger_graphic)

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    sk = 2
    pk = G + G

    print("")

    print(Fore.LIGHTYELLOW_EX + f" Secret Key: {sk} \n"
          f" Public Key: \n "
                f"{(pk.x, pk.y)} \n "
    )

    # Verfication public key
    time.sleep(1.0)
    print(f"Verify that Public Key is on the Curve: ",
          (public_key.y ** 2 - public_key.x ** 3 - 7) %
          bitcoin_curve.p == 0
    )

    # Add another to chain
    time.sleep(1.0)

    openLedger_graphic2 = pyfiglet.figlet_format("                 True Genesis Block \n")

    print("")

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    print(Fore.LIGHTBLUE_EX + openLedger_graphic)

    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    # All of that is created a crytographic identity, now we know the structure is working
    # We can make the Merkle Tree, do actual hashing functions on 32 bit words
    sha256 = gen_sha256_with_variable_scope_protector_to_not_pollute_global_namespace()
    print("Verify Empty Hash: ", sha256(b" ").hex())

    print("")

    #print(sha256, (b"").hex())





#    sk = 3
#    pk = G + G + G

#    print("") # toDo --> Print out timestamps on each of these 'Sleeping-Points'
              #          so must use datetime Python Library. . .

#    print(f" Secret Key: {sk} \n"
#          f" Public Key: \n "
#              f"{(pk.x, pk.y)} \n "
#    )

    # Verfication public key
#    print(f"Verify that Public Key is on the Curve: ",
#          (pk.y ** 2 - pk.x ** 3 - 7) %
 #         bitcoin_curve.p == 0
 #   )

#    print("") # toDO --> Print out timstamping using datetime library

    # Add another to chain
 #   time.sleep(1.0)

 #   sk = 4
#    pk = G + G + G + G

#    print(f" Secret Key: {sk} \n"
#          f" Public Key: \n "
#              f"{(pk.x, pk.y)} \n "
 #   )

    # Verfication public key
    #time.sleep(1.0)
    #print(f"Verify that Public Key is on the Curve: ",

          # toDo --> Error Testing Diagnostics for "Honey-Pot"
          #          So if soemthing goes here, engage Honey-Pot
          #          like "Cold-Vault" FOrk Sequence to offline Wallet

          #(pk.y ** 2 - pk.x ** 3 - 7) % # Try mess around here and see what it does...
              #bitcoin_curve.p == 0
    #)

    #print("")



#    # Add another to chain
#    time.sleep(1.0)

#    sk = 5
#    pk = G + G + G + G + G

#    print("")

#    print(f" Secret Key: {sk} \n"
#          f" Public Key: {(pk.x, pk.y)} "
#    )

    # Verfication public key
#    print(f"Verify that Public Key is on the Curve: ",
#          (pk.y ** 2 - pk.x ** 3 - 7) %
#          bitcoin_curve.p == 0
#    )

    print("")
    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")
    print(Fore.LIGHTBLUE_EX + footer_for_logger)
    print(Fore.MAGENTA +
          "# * $ * ================================================================ * $ * #")

    # * --------------------------------------------------------- * #
    #   Ending of Chaining and pairing Private and Public Keys on
    #   a Public Domain of a Digital and Open LedgeR
    # * --------------------------------------------------------- * #

# * -------------------------------------------------------------------- * #
if __name__ == '__main__':
    main()
# * -------------------------------------------------------------------- * #

# * ========================================================================== * #
#                                   EnND ( !! )
# * ========================================================================== * #
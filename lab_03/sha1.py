from struct import pack
from typing import Iterable, List, Union

BITS_IN_BYTE = 8
BITS_IN_WORD = 32
MSG_BLOCK_SIZE = 512

def rotl(x: int, n: int) -> int:

    return ((x << n) | (x >> 32 - n)) & 0xffffffff


# SHA-1 functions
def ch(x: int, y: int, z: int) -> int:
    
    return (x & y) ^ (~x & z)

def parity(x: int, y: int, z: int) -> int:
    
    return x ^ y ^ z

def maj(x: int, y: int, z: int) -> int:
    
    return (x & y) ^ (x & z) ^ (y & z)


def pad_message(msg: Union[str, bytes]) -> bytes:
    
    # Convert message to bytes if string is provided
    if type(msg) is str:
        msg = msg.encode()

    # Get message length in bits
    ln = len(msg) * BITS_IN_BYTE

    # Zeros to append to message
    k = (448 - ((ln + 1) % 512)) % 512

    # Message format
    fmt = f'>{len(msg)}sc{(k - 7) // 8}sQ'

    # Return padded message
    return pack(fmt, msg, b'\x80', b'', ln)


def parse_message(msg: bytes) -> Iterable[List[int]]:

    for i in range(0, len(msg) * BITS_IN_BYTE // MSG_BLOCK_SIZE):

        # Compute word start indexes
        WS = [i * 64 + j * 4 for j in range(0, MSG_BLOCK_SIZE // BITS_IN_WORD)]

        # Yield new message block (sixteen 32-bit words)
        yield [int.from_bytes(msg[ws:ws + 4], 'big') for ws in WS]


# Hash Computation
def process_block(Mi: List[int], H: List[int]) -> List[int]:

    # Make sure block has 16 words
    assert len(Mi) == 16

    # 1. Prepare message schedule
    W = Mi.copy()
    for t in range(16, 80):
        W += [rotl(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], 1)]

    # 2. Initialize working wariables
    a, b, c, d, e = H

    # 3. Calculate hash
    for t in range(80):

        f = F[t // 20](b, c, d)
        k = K[t // 20]

        tmp = rotl(a, 5) + f + e + k + W[t] & 0xffffffff
        e, d, c, b, a = d, c, rotl(b, 30), a, tmp

    # Compute intermediate hash value
    for i, x in  enumerate([a, b, c, d, e]):
        H[i] = (H[i] + x) & 0xffffffff

    return H


# SHA-1 Functions
F = [ch, parity, maj, parity]

# SHA-1 Constants
K = [0x5a827999, 0x6ed9eba1, 0x8f1bbcdc, 0xca62c1d6]


def sha1(msg: Union[str, bytes]) -> str:

    # 1. Preprocessing: Padding -> Parsing -> Set Initial Hash Value
    msg = pad_message(msg)
    M = parse_message(msg)
    H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]
    
    # 2. Compute hash on message blocks
    for Mi in M:
        H = process_block(Mi, H)

    # 3. Return message digest (i.e. hash value)
    return ''.join(hex(x)[2:] for x in H)

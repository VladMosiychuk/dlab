import hashlib
from sha1 import sha1

test_messages = ['abc', 'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq', 'hello world', '😎😎😎😎']

print(f'My SHA-1 {" " * 31} | Builtin SHA-1{" " * 27} | Message')
for msg in test_messages:

    my_hash = sha1(msg)
    builtin_hash = hashlib.sha1(msg.encode())

    print(f'{my_hash} | {builtin_hash.hexdigest()} | {msg}')
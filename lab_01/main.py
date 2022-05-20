import time
from random import randint
from itertools import count

# Task #1
def get_combinations_cnt(key_length: int) -> int:
    return 2 ** key_length

# Task #2
def get_random_key(key_length: int) -> int:
    return randint(0, get_combinations_cnt(key_length) - 1)

# Task #3
def bruteforce_time(key: int) -> float:

    # Start timer
    st = time.time()
    
    # Find key 
    for n in count():
        if n == key:
            break

    # Return execution time in ms
    return (time.time() - st) * 1000


key_lengths = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
key_combs = [*map(get_combinations_cnt, key_lengths)]
rand_keys = [*map(get_random_key, key_lengths)]

for kl, kc, rk in zip(key_lengths, key_combs, rand_keys):

    print(f'Key length (bit)     : {kl}')
    print(f'Combinations count   : {kc}')
    print(f'Random key           : {rk}')
    print(f'Bruteforce time (ms) : {bruteforce_time(rk):.4f}')
    print('-' * 22)
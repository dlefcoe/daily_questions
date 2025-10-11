#!/usr/bin/env python3

from hashlib import sha256

message1 = "This is the input message blah blah"
message2 = "This is the input message blah blaG"


def hash_it_up(message:str):
    ''' Brute force a sha256 hash to find a number that matches the first 3 characters of the hash of the input message.'''
    hashed = sha256(message.encode()).hexdigest()
    print(hashed)

    x = 0

    while True:
        x += 1
        attempt = sha256(str(x).encode()).hexdigest()
        if attempt[:3] == hashed[:3]:
            print(attempt)
            print(f'Cracked after {x} attempts')
            break


hash_it_up(message1)
hash_it_up(message2)


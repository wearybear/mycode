#!/usr/bin/env python3

import time

def bottles_of_beer(num_bottles):
    while num_bottles > 0:
        print(f"{num_bottles} bottles of beer on the wall!")
        time.sleep(1)
        print(f"{num_bottles} bottles of beer on the wall! {num_bottles} bottles of beer! You take one down, pass it around!")
        time.sleep(1)
        num_bottles -= 1
        if num_bottles > 0:
            print(f"{num_bottles} bottles of beer on the wall!")
            time.sleep(1)

bottles_of_beer(99)


# JM

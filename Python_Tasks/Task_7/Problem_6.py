#!/bin/python3

import math
import os
import random
import re
import sys

# Q6. Pangrams
# HackerRank Link:
# https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())

    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in letters:
            return "not pangram"

    return "pangram"


if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
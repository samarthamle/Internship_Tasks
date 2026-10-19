#!/bin/python3

import string

# Q7. Alphabet Rangoli
# HackerRank Link:
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]

        row = "-".join(left + right)
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines[:0:-1] + lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
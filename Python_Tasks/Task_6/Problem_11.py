# Q11. String Formatting

# HackerRank: https://www.hackerrank.com/challenges/python-string-formatting/problem

from os import name

from numpy import number


def print_formatted(number):
    width = len(bin(number)[2:])


for i in range(1, number + 1):
    decimal = str(i)
    octal = oct(i)[2:]
    hexadecimal = hex(i)[2:].upper()
    binary = bin(i)[2:]

    class width:
        ...

    print(decimal.rjust(width),
          octal.rjust(width),
          hexadecimal.rjust(width),
          binary.rjust(width))


if name == 'main':
    n= int(input())
    print_formatted(n)


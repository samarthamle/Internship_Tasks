# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_sizes = Counter(map(int, input().split()))

n = int(input())
total_earnings = 0

for i in range(n):
    size, price = map(int, input().split())

    if shoe_sizes[size] > 0:
        total_earnings += price
        shoe_sizes[size] -= 1

print(total_earnings)
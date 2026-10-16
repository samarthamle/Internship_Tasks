# Problem: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
countries = set()

for i in range(n):
    countries.add(input())

print(len(countries))
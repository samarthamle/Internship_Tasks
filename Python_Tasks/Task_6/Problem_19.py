# Q19. Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

import collections

s = input()

counter = collections.Counter(s)

for char, count in sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:3]:
    print(char, count)

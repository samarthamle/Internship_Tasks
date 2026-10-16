# Problem: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

word_count = {}

for i in range(n):
    word = input()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(*word_count.values())

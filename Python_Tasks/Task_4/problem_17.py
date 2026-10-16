# Problem: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}

for i in range(n):
    name, *marks = input().split()
    students[name] = list(map(float, marks))

query_name = input()

average = sum(students[query_name]) / len(students[query_name])

print(f"{average:.2f}")
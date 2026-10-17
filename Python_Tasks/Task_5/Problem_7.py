# Problem_7:Symmetric Difference
#  HackerRank:https://www.hackerrank.com/challenges/symmetric-difference/problem

n = int(input())
set_m = set(map(int,input().split()))

n = int(input())
set_n = set(map(int,input().split()))

result = set_m.symmetric_difference(set_n)
for num in sorted(result):
    print(num)
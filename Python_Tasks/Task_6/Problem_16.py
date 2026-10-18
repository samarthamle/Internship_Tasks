# Q16. Check Subset
# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(input())
for _ in range(T):
    a = int(input())
    A = set(map(int,input().split()))
    
    a = int(input())
    B = set(map(int,input().split()))
    print(A.issubset(B))
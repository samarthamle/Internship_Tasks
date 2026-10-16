# Problem: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    score = sorted(set(arr),reverse= True)
    print(score[1])
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [0 for _ in range(M)]
res = 0

for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(M):
        table[i] += line[i]

A = int(input())

for i in range(M-A+1):
    res = sum(table[i:i+A]) if sum(table[i:i+A])>res else res

print(res)

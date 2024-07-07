import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n = list(map(int, input().split()))
sn = []

for i in range(N-K+1):
    sn.append(sum(n[i:i+K]))

print(max(sn))

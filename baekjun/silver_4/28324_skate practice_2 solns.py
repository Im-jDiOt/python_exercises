# sol1
import sys

input = sys.stdin.readline
n = int(input())
v = list(map(int, input().split()))
limit = list(range(n, 0, -1))
res = []

for i in range(n):
  res.append(min(v[i], limit[i]))

for i in range(n-1, 0, -1):
  res[i-1] = min(res[i-1], res[i]+1)

print(sum(res))

# sol2 (other's)
def solution():
    N = int(input())
    V = tuple(map(int, input().split()))
    res = speed = 0
    for i in range(N-1, -1, -1):
        if V[i] > speed:
            speed += 1
        elif V[i] < speed:
            speed = V[i]
        res += speed
    print(res)

solution()

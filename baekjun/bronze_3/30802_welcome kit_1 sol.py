N = int(input())
needs = list(map(int, input().split()))
T, P = list(map(int, input().split()))
res = 0

for n in needs:
    s, r = divmod(n, T)
    if r: res += s+1
    else: res += s

print(res)
print(*divmod(N, P))

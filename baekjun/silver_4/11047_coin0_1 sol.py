import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
cnt = 0

for i in range(N):
    c = int(input())
    if c<=K: coin.append(c)
    else: break

while K!=0:    
    if K-coin[-1]>=0:    
        cnt += K//coin[-1]
        K = K%coin[-1]
    else:
        pass
    coin.pop(-1)

print(cnt)

# 한 번에 풀어서 기분이 좋다...ㅎ

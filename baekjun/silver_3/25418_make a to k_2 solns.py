# sol1
A, K = map(int, input().split())
cnt = 0

while A != K:
    if K%2 == 0:
        K /= 2
        if K<A:
            cnt += K*2-A 
            break 
    else:
        K -= 1
        
    cnt += 1

print(int(cnt))

# 만약 도달수가 홀수라면 -> -1 
# 만약 도달수가 짝수라면 -> /2 -> 만일 K가 A보다 작아진다면 그때부턴 -1만
# 9 32 / 32, 16, 8(x) -> 16 15 14 13 12 11 10 9

# sol2 (other's)(BFS)
from collections import deque
A,K = map(int,input().split())

que = deque([(A,0)])
vis = [0]*1000001
while que:
    q = que.popleft()
    if q[0] == K:
        print(q[1])
        break
    if vis[q[0]]:
        continue
    vis[q[0]] = 1
    if q[0]*2<=K:
        que.append((q[0]*2,q[1]+1))
    if q[0]+1<=K:
        que.append((q[0]+1,q[1]+1))

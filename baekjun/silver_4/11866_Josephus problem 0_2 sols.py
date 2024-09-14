import sys
input = sys.stdin.readline

N, K = map(int, input().split())

'''
.
1 2 3 4 5 6 7 (pos=0)
(pos=pos+K-1=2)
-> pop(pos) = pop(2) = 3 
    .
1 2 4 5 6 7 
        .
1 2 4 5 7 -> 3,6 (pos=pos+K-1=4)
(pos'=pos+K-1=6) > len(L)-1 = 4
pos'' = pos'-(len(L)-1)-1 = 1
-> pop(pos'') = pop(1) = 2
1 4 5 7 -> 3,6,2 
pos' = 1+3-1=3 <= len(L)-1=3
-> pop(pos')
1 4 5 -> 7

...
(l:list)에서 K번째를 빼냄. -> l을 deque로 구현하면 rotate 쓰면 되지 않을까 싶음.
만약 빼내야할 index가 전체 길이를 넘어선다면
(K - 남은 인덱스 개수)만큼의 인덱스 위치의 요소를 빼냄?

'''

L = list(range(1,N+1))
pos = 0
ans = []

def init_pos(pos):
    while pos>len(L)-1:
        pos -= len(L)
    return pos

while L:
    init_pos(pos)
    pos = pos+K-1
    if pos<=len(L)-1: pass
        # ans.append(str(L.pop(pos)))
        # print(L.pop(pos), end='//')

    else:
        pos = init_pos(pos)
        # ans.append(str(L.pop(pos)))
        # print(L.pop(pos), end='//')
    ans.append(str(L.pop(pos)))
    

    # print(L, '//', pos)
    # print('===============')

print('<',', '.join(ans),'>', sep='')
'''
1 3
-> index error
'''

# sol2 -> init_pos 이 부분 그냥 % 쓰면 됐는데.. 멍청해라...
import sys
n, k = map(int, sys.stdin.readline().split())
idx = 0
queue = [i for i in range(1, n+1)]
res = []

while queue:
    idx += k - 1
    if idx >= len(queue):
        idx %= len(queue)
    res.append(str(queue.pop(idx)))
print("<", ", ".join(res), ">", sep="")

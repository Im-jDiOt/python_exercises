import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
city = [input().split() for _ in range(M)]
visited = deque([(0,0)])


#print(city)

while visited:
    pos = visited.pop()
    if pos == (N-1, M-1):
        print('Yes')
        sys.exit()
    if pos[0]<N-1 and int(city[pos[1]][pos[0]+1]):
        city[pos[1]][pos[0]] = 0
        visited.append((pos[0]+1, pos[1]))
    if pos[1]<M-1 and int(city[pos[1]+1][pos[0]]):
        city[pos[1]][pos[0]] = 0
        visited.append((pos[0], pos[1]+1))

print('No')

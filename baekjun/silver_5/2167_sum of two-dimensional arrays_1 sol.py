import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prefix = []
k = 0

for _ in range(N):
    one_line = list(map(int, input().split()))
    prefix.append(0)
    k = 0
    for n in one_line:
        k += n
        prefix.append(k)

K = int(input())

for _ in range(K):
    pos = list(map(int, input().split()))
    sum = 0

    y1, x1 = pos[0], pos[1]
    y2, x2 = pos[2], pos[3]

    for y in range(y1-1, y2): 
        sum += prefix[x2+y*(M+1)] - prefix[x1-1+y*(M+1)]
    
    print(sum)

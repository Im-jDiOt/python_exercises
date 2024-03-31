# sol1

import sys

N, M = map(int, input().split())
a = [list(input()) for _ in range(2*N)]

for i in range(N):
    for j in range(M):
        if a[i][j] == a[i+N][2*j] == a[i+N][2*j+1]:
            pass
        else:
            print("Not Eyfa")
            sys.exit()
            
print("Eyfa")


# sol2(other's) : 두 개씩 검사

n,m = map(int,input().split())
fir = [input() for _ in range(n)]
sec = [input() for _ in range(n)]

res = True

for i in range(n):
    tmp1 = fir[i] == sec[i][0::2]
    tmp2 = fir[i] == sec[i][1::2]

    res &= tmp1 & tmp2

print("Eyfa" if res else "Not Eyfa")


# sol3(other's) : 돌돔에서 뚊 만들고 검사

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = []
b = []

for _ in range(n):
    c = input().rstrip()
    v = ''

    for x in c:
        v += x + x

    a.append(v)

for _ in range(n):
    c = input().rstrip()
    b.append(c)

if a == b:
    print('Eyfa')
else:
    print('Not Eyfa')

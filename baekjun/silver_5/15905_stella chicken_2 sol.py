# sol1
import sys
input = sys.stdin.readline

l = []
i = 5
cnt = 0

N = int(input())

# 이 부분 리스트 컴프리헨션으로 (sol2 참고)
for _ in range(N):
    q, p = map(int, input().split())
    l.append([q,p])

l.sort(key=lambda x: (-x[0], -x[1]))

while True:
    if i==N: break
    if l[4][0] == l[i][0]:
        cnt += 1
        i += 1
    else: break

print(cnt)


# sol2
N=int(input())
a=[input().split() for _ in range(N)]

a.sort(key=lambda x: (-int(x[0]), int(x[1])))
five = a[4][0]
cnt=0
for i in range(N):
    if i > 4:
        if a[i][0]==five:
            cnt+=1
print(cnt)

# sol1
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1,y1, r1, x2,y2, r2 = map(int, input().split())
    d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

    def abs(x):
        return x if x>=0 else -x

    if x1==x2 and y1==y2 and r1==r2: print(-1)
    elif d<r1 or d<r2:
        if d==abs(r2-r1): print(1)
        elif d>abs(r2-r1): print(2)
        else: print(0)
    else:
        if d==r1+r2: print(1)
        elif d<r1+r2: print(2)
        else: print(0)

# sol2 -> 조건문의 순서와 abs를 제곱으로 처리
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dist = (x1-x2)**2+(y1-y2)**2
    R = (r1 + r2)**2
    if (x1==x2) & (y1==y2) & (r1==r2) :
        if r1 == 0 :
            print(1)
        else :
            print(-1)
    elif ((x1==x2) & (y1==y2)) | (R < dist) | (dist**0.5+min(r1,r2) < max(r1,r2)):
        print(0)
    elif (R == dist) | (dist**0.5+min(r1,r2) == max(r1,r2)) :
        print(1)
    else :
        print(2)

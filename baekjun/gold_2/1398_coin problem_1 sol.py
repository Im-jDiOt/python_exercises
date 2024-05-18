# sol1 -> 다른 풀이 꼭 공부하기... 너무 무식하게 밀어붙임..

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 0
    P = list(map(int, list(input().rstrip())))
    while P:
        if len(P)%2: cnt += P[0]; del P[0]
        else:
            if P[0]<=1 or (P[0]==2 and P[1]<5):
                cnt += P[0]+P[1]

            elif P[0]==2:
                cnt += P[1]-4

            elif P[0]==3:
                if P[1]<5:
                    cnt += P[1]+3
                else:
                    cnt += P[1]-3

            elif P[0]==4:
                if P[1]<5:
                    cnt += P[1]+4
                else:
                    cnt += P[1]-2

            elif P[0]==5:
                if P[1]<5:
                    cnt += P[1]+2
                else:
                    cnt += P[1]-1

            elif P[0]==6:
                if P[1]<5:
                    cnt += P[1]+3
                else:
                    cnt += P[1]

            elif P[0]==7:
                if P[1]<5:
                    cnt += P[1]+4
                else:
                    cnt += P[1]-2
    
            elif P[0]==8:
                if P[1]<5:
                    cnt += P[1]+5
                else:
                    cnt += P[1]-1

            else:
                if P[1]<5:
                    cnt += P[1]+6
                else:
                    cnt += P[1]
            del P[0]; del P[0]
             
    print(cnt)
    

import sys
input = sys.stdin.readline

P = [1,1,1,2,2]
T = int(input())

for _ in range(T):
    N = int(input())
    l = len(P)
    
    if N<=l:
        print(P[N-1])
    else:
        for _ in range(N-l):
            P.append(P[-1] + P[-5])
        print(P[-1])
      
# 풀이 과정
# 1 1 1 2(2,3) 2 3(1,5) 4(2,6), 5(3, 7), (4,8)2+5 = 7, 9, 12

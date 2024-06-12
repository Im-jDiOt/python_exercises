import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = 0

for i in range(N):
    sum += P[i]*(N-i)
    
print(sum)

# so ez..ㅋㅋㅋㅋ 에휴

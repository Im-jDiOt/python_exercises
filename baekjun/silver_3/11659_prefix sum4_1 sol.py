import sys
input = sys.stdin.readline

N, M = map(int,input().split())
l = list(map(int, input().split()))
s = []
k = 0

for i in l:
    k += i
    s.append(k)
s.insert(0, 0)

for _ in range(M):
    i, j = map(int, input().split())
    print(s[j]-s[i-1])  
# 리스트에 N개 수 입력받을 때 시그마(1~N) 값으로 리스트에 저장하기
# i,j 입력받으면 j-1번째 값에서 i번째 값을 빼서 출력하기 -> 0번째 값을 0으로 넣으면서 하나씩 밀림

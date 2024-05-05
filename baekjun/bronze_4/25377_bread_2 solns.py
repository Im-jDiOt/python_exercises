# sol1
N = int(input())
min = 1001

for _ in range(N):
  n,m = map(int, input().split())
  if n>m:
    continue
  else:
    min = (m if m<min else min) # min = min(m, min)

print(min if min<=1000 else -1)


# sol2(other's)
import sys

n = int(sys.stdin.readline())
result = list()

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a <= b:
        result.append(b)

try:
    print(min(result))  # 에러가 발생할 것 같은 코드
except:
    print(-1)  # 에러 발생 시 실행될 코드
#if문보다 약간 느리다는 단점이 있지만 예외 부분을 유연하게 처리하여 좀더 쉽게 코드를 작성할 수 있다는 장점이 있다. 

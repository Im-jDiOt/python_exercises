# try1 : 제출 전 테스트3에서 안 됨을 깨닫고 sol1을 작성함
A, B, V = map(int, input().split())
height = 0
cnt = 0

while True:
  height += A
  cnt += 1
  if height >=  V: break
  else: height -= B

print(cnt)

# sol1
import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)

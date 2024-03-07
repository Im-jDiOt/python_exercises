# try1: 메모리 초과
import sys
input = sys.stdin.readline
numbers =[]

for _ in range(int(input())):
  numbers.append(int(input()))

print(*sorted(numbers), sep='\n')

# int 자료형 데이터 갯수에 따른 메모리 사용량

# 데이터 갯수	메모리사용량
# 1,000	약 4KB
# 1,000,000	약 4 MB
# 10,000,000	약 40MB -> 8mb 제한이라 걸림
# 출처: https://velog.io/@yesterdaykite/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%ED%81%AC%EA%B8%B0

# sol1
import sys 
input = sys.stdin.readline
numbers = [0 for _ in range(10000)]

for _ in range(int(input())):
  numbers[int(input())-1] += 1

for i in range(10000):
  if numbers[i]:
    for _ in range(numbers[i]): 
      print(i+1)
  else: pass



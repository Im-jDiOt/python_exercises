# https://www.acmicpc.net/problem/1075

# sol1
import sys

N, F = int(input()), int(input())
N2 = int(N/100)*100

for i in range(10):
    for j in range(10):
        if (N2+10*i+j)%F == 0:
            print(str(N2+10*i+j)[-2:])
            sys.exit()
            
# sol2(other's) : 잘 모르겠는데 그렇다고 한다. 이해는.. 미래의 내게..
x=int(input())
y=str(x)[-2:]
N=int(x)-int(y)
F=int(input())
while True:
    if N%F==0:
        break
    N+=1
print(str(N)[-2:])

# sol3(other's) : 아 굳이 for 중첩할 필요가 없었네... am 5라 머가리가 안 돌아가서.... 그런 거라기엔 뭐ㅎ jdiot 닉값 어디가겠나ㅎㅎ
N = int(input())
M = int(input())

last_two = N % 100

N00 = N - last_two

for i in range(N00, N00 + 100):
    if i % M == 0:
        result = i % 100
        if result < 10:
            print(f'0{result}')
            break
        else:
            print(result)
            break

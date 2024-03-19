# sol1
N = int(input())
fac = 1
cnt = 0

for i in range(1, N+1):
    fac *= i

for i in range(1, len(str(fac))+1):
    if str(fac)[-i] == '0': cnt += 1
    else: break
    
print(cnt)

# sol2 (other's)
N = int(input())
fac = 1
cnt = 0
j = -1

for i in range(1, N+1):
    fac *= i
    
while True:
    fac = str(fac)
    if fac[j] == '0': cnt += 1; j -= 1
    else: break
    
print(cnt)

# sol3 (other's) : ...????????
N=int(input())
print(N//5 + N//25 + N//125)



# sol1, sol2에서 for문 통한 index 탐색 vs while문 통한 index 탐색 중에 뭐가 더 효율적일까?
# sol3 : 결국 0의 개수를 구한다 == 10이 얼마나 곱해지는지를 구한다 == 곱해진 5의 개수를 구한다 와 같다. 이 때 N의 범위가 500까지 이므로 125(=5^3)까지만 했을 때 해서 구하면 된다.

import sys
input = sys.stdin.readline

N = int(input())
xs = list(map(int, input().split()))
dxs = {}
for i,k in enumerate(sorted(set(xs))):
    dxs[k] = i

for x in xs:
    print(dxs[x], end=' ')

# sol2 -> 코드는 비슷한 거 같은데 시간차가 많이 남..
# sys.stdin.buffer.read()가 더 빠른가봄?
# 그리고 컴프리헨션!
import sys
stdin = sys.stdin.buffer

stdin.readline()
arr = list(map(int, stdin.read().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join(map(str, [dic[x] for x in arr])))



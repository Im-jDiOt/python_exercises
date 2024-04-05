# sol1 : 그냥 문제 직독직해..
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(range(1,n+1))
    
    for i in range(n):
        if a[i] != b[i]: continue
        else:
            b[i:] = list(map(lambda x: x+1, b[i:]))
    
    print(b[-1])
    
# sol2(other's) : 어케 바로 구할 생각을 할까.....ㅜㅠ
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    good_num = 0
    for i in range(len(seq)):
        good_num += 1
        while good_num == seq[i]:
            good_num += 1

    print(good_num)

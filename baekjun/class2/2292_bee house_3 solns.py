# sol1 : 아 수열 귀찮다고 맨날 귀납적으로 푼 게 여기서 들통나네..
N = int(input()) - 1
k = 6
cnt = 1

while N > 0:
    N = N - k
    k += 6
    cnt += 1
    
print(cnt)

# sol2(other's) : 비슷한데 더 깔쌈한 느낌
n = int(input())
nums_pileup = 1
cnt = 1

while n > nums_pileup :
    nums_pileup += 6 * cnt
    cnt += 1
    
print(cnt) 

# sol3(other's) : 코드를 보고도 바로 안 와닿는데 이걸 어떻게 생각해내냐.. 참내!
print(round(((int(input())-1)/3)**0.5)+1)

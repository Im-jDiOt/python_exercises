import sys
input = sys.stdin.readline

N = int(input())
nums = []
numsdict = {}
mv = 0
mk = []

for _ in range(N):
    n = int(input())
    nums.append(n)
    if n in numsdict: numsdict[n] += 1
    else: numsdict[n] = 1

for k, v in numsdict.items():
    if mv > v:
        pass
    elif mv == v:
        mk.append(k)
    else:
        mv = v
        mk = []
        mk.append(k)

mk.sort()
nums.sort()

# 최빈값을 어떻게 찾으면 좋을까
# 가장 빈번히 나오는 값을 찾아야 돼
# 빈번함이 많은 게 여러 개라면 그 중 두 번째로 작은 값을 찾아야 돼
# 그 말은 음 횟수를 기록하고 그 횟수와 수를 연결 지어서 볼 수 있으면 좋을 거 같은데
# 그러면 해쉬 자료형 즉 dict를 써야겠지
# 그러면 처음에 nums를 기록할 때부터 dict로 하면 안되나
# 아니면 nums 리스트는 따로 만들고 dict는 또 따로 해서...

# 일단 그럼 dict로 하는 걸로?
# 근데 dict로 해도
# 키에서 값을 찾는 게 빠른 거지 결국에는 value를 또 돌아야 돼
# 사실 다 돌아도 문제는 풀 수 있을 거 같긴 해..

# mk의 리스트 길이가 1일 경우의 수 
# 1) N == 1
# 2) 2회 이상 나오는 게 있고 그게 한 개일 때

# print(nums)
# print(numsdict)
# print(mk)

print(round(sum(nums)/N))
print(nums[int((N-1)/2)])
print(mk[1] if len(mk)>1 else mk[0])
print(max(nums)-min(nums))

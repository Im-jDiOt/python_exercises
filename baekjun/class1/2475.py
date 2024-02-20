#sol1
print(sum(map(lambda x: int(x)**2, input().split()))%10) 

#sol2 (other's code)
print(sum(int(n)**2 for n in input()[::2]%10))

#sol3
print(sum(int(n)**2 for n in input().split())%10)

# input().split() 쓰면 map()부터 쓰고보는 관성...
# 근데 그러면 한 라인 인풋 정수로 바꿀 때에도 map 안 쓰고
# [int(n) for n in input().split()]
# 요래 해주면 되는 거 아닌가? 어떨 때 map이 유리한거지?

# https://switowski.com/blog/map-vs-list-comprehension/
# 요약: 이미 내장된 함수를 이용할 때에는 map을, 그 외 lambda를 써야할 때에는 list comprehension이나 generator expression을 사용하는 것이 더 빠르다.
# 즉, int라는 이미 내장된 함수를 쓸 때에는 map을 쓰는 게 더 빠른 방법이고 이 문제에서와 같이 lambda를 쓸 경우엔 list comprehension이 더 빠른 방법이다.

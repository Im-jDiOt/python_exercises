# sol1 : range
N = int(input())
print(*range(1, N+1), sep='\n')

# sol2 : list comprehension
N = int(input())
print(*[n for n in range(1, N+1)], sep='\n')

# sol3(other's) : 내 sol1이 더 깔쌈하지 않..나..! 
N = int(input())
print("\n".join(map(str, range(1, N + 1))))

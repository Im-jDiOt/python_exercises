# sol1 : for loop
N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")
    #print(N, '*', i, '=', a*i)
    
# sol2 : list comprehension
N = int(input())
print(*[f"{N} * {i} = {N*i}" for i in range(1, 10)], sep='\n')

# sol3 (other's) : exec()
n, i = int(input()), 1
exec("print(n, '*', i, '=', n*i); i+=1;"*9)

# 형식에 맞춰 출력하는 문제라고 무조건 f-string 쓸 생각하지 말자!
# eval만 알았는데 exec이라는 함수도 있나봄

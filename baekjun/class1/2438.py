#sol1 : used for loop
N = int(input())
for i in range(1, N+1):
    print('*'*i)

#sol2 : used while loop
i = 1
N = int(input())
while i <= N:
    print('*'*i)
    i+=1
    
#sol3 : used list comprehension
N = int(input())
print(*['*'*i for i in range(1, N+1)], sep='\n')

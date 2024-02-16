#sol1
A, B = map(int, input().split())
print(A-B)

#sol2
problem = input().split()
problem.insert(-1, '-') 
print(eval(''.join(problem)))

#(0)A(1)B(2), (-2)A(-1)B <- how 'python insert' counts indexes.

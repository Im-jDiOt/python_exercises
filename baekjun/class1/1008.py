# sol1
A, B = map(float, input().split())
print(A/B)

# sol2
A, B = input().split()
print(eval(''.join([A, '/', B])))

# used eval() and variables.
# similar with 1001 sol2 but this used variables instead of insert()
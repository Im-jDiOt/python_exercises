# sol1
A, B = input().split()

delta = len(B)-len(A)
ldiff = []

for i in range(delta+1):
    diff = 0
    for j in range(len(A)):
        if A[j] != B[j+i]: diff+=1
    ldiff.append(diff)

print(min(ldiff))


# sol2 (other's)
result=51

a,b=input().split()

for y in range(len(b)-len(a)+1):
    n=0
    for x in range(len(a)):
        if(a[x]!=b[x+y]):
            n+=1
    if(result>n):
        result=n

print(result)

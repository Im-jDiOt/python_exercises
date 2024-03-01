# sol1
L, my_string = int(input()), input()
sum = 0

for i in range(L):
    sum += (ord(my_string[i])-96)*(31**i)
    
print(sum%1234567891)

# sol2(other's)
input()
print(sum((ord(n)-96)*31**m for m,n in enumerate(input()))%1234567891)

# enumerate()를 이렇게 사용하면 코드가 깔삼해지는구나..!

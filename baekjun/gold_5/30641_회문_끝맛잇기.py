L, U = map(int, input().split())
MOD = 10**9+7
inv25 = pow(25, MOD-2, MOD)

L_is_odd = L%2
U_is_odd = U%2
i = int((L-1)//2)
j = int((U-1)//2)

a = pow(26, i, MOD)
b = pow(26, j-i+1, MOD)
t = (b-1+MOD) % MOD
num = (2*a*t)%MOD
num = (num*inv25)%MOD

if not L_is_odd: num -= 26**i
if U_is_odd: num -= 26**j

print('H' if L==2 or (L==1 and U==1) else 'A')
print(num%(10**9+7))

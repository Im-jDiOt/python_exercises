#sol1
A, B = map(int, input().split())
if A>B: print('>')
elif A<B: print('<')
else: print('==')

#sol2
A, B = input().split()

for sign in ['>', '<', '==']:
    if eval(A+sign+B):
        print(sign)
        break
    else: pass

#sol3 (other's code)  
a, b = map(int, input().split())
print(['><'[a < b], '=='][a == b])
# 개쩐다...
# used int(boolean) and list, string index

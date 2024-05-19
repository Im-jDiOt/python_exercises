# sol1
N, P, Q = map(int, input().split())

element_set = {N}
seq_dict = {}
min = min(P,Q)

if N==0:
    print(1)
else:
    while element_set:
        n = element_set.pop()
        if n>0:
            seq_dict.update({n : [n//P, n//Q]})
            element_set.update([n//P, n//Q])
        else:# n==0
            seq_dict.update({n : 1})
        
    sorted_dict = dict(sorted(seq_dict.items()))

    for key, value in sorted_dict.items():
        if type(value)==int: continue
        else:
            sorted_dict[key] = sorted_dict[value[0]]+sorted_dict[value[1]]

    print(sorted_dict[N])

# sol2(other's)
def f(i):
    if i in d: return d[i]
    else: d[i]=f(i//p)+f(i//q)
    return d[i]
n,p,q = map(int, input().split())
d={0:1}
print(f(n))

# try - 뭔가 sol2 이 풀이에 dict 결합시킨 느낌.. 나 너무 더럽게 풂ㅋㅋㅋ..ㅜㅠ
N, P, Q = map(int, input().split())

mn = min(P,Q)
mx = max(P,Q)

def A(n):
    if n==0: return 1
    elif n<mn: return 2
    elif n==mn: return 3
    else: return A(int(n/mn))+A(int(n/mx))

print(A(N))

T = int(input())

for _ in range(T):
    zero = [1,0]
    N = int(input())
    if N==0:
        print(zero[N], zero[N+1])
        continue
    else:
        for _ in range(N):
            zero.append(zero[-2]+zero[-1])
    
    print(zero[-2], zero[-1])

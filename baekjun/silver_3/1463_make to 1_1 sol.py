# 1 0
# 2 1
# 3 1
# 4 4/2=2(=1), 2
# 5 5-1=4(=2), 3
# 6 6/3=2(=1), 2
# 7 7-1=6(=2), 3
# 8 8/2=4(=2), 3
# 9 9/3=3(=1), 2
# 10 10/2=5(=3), 4 vs 10-1=9(=2), 3
# ...

# N까지 쭉 돌려보나..?
N = int(input())
d = {1:0, 2:1, 3:1, 4:2, 5:3, 6:2, 7:3, 8:3, 9:2, 10:3}
if N<11:
    print(d[N])
else:
    for n in range(11, N+1):
        k = []
        cnt = 1000000
        if n%2==0: k.append(n/2)
        if n%3==0: k.append(n/3) # elif로 쓰면 안 됨..
        k.append(n-1)
        for key in k:
            cnt = d[key]+1 if d[key]+1<cnt else cnt
        d[n] = cnt
        
    print(d[N])

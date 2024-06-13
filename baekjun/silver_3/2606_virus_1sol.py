import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
computer = {i:0 for i in range(1, N+1)}
room = 1

for x in range(M):
    a, b = map(int, input().split())
    if computer[a]+computer[b]==0:
        computer[a] = computer[b] = room
        room += 1
    elif computer[a]*computer[b] == 0:
        if computer[a]==0: computer[a]=computer[b]
        else: computer[b]=computer[a]
    else:
        if computer[a]==computer[b]: continue
        elif computer[a]<computer[b]: p,q = a,b
        else: p,q=b,a
        l = []
        for k,v in computer.items():
            if v == computer[q]:
                l.append(k)
        for i in l:
            computer[i]=computer[p]

            
    # print(x, end='  ')
    # print(computer)

cnt = -1
for k,v in computer.items():
    if v==computer[1]: 
        cnt += 1
print(cnt)
        

    # 만약 방 번호 둘 다 == 0이라면 
    # 가장 최신 방으로 옮겨주기
    # 만약 방 번호 하나만 0이고 하나는 0이 아니라면
    # 0이 아닌 방 번호로 0인 방 번호를 채워주기
    # 만약 둘 다 0이 아니라면
    # 둘 중 작은 번호로 통일해서 채워주고
    # 둘 중 큰 번호였던 것 또한 작은 번호로 채워주기
    
    # 이렇게 다 채우고 1번 컴퓨터와 같은 방번호인 컴퓨터의 개수 찾아주기
    
    
    

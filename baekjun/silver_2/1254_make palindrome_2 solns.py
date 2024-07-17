# sol1
S = list(input())
rS = list(reversed(S))
start = []

# rS의 첫 글자와 같은 글자를 S에서 찾는다.
for i in range(len(S)): 
    if rS[0] in S[i]:
        start.append(i)

# 만약 찾은 글자가 S의 마지막 글자라면 2*len-1을 출력하고 끝낸다.
if start[0] == len(S)-1:
    print(len(S)*2-1)

# 만약 찾은 글자가 여러개라면
# rS는 인덱스 1부터, S는 그 찾은 글자의 인덱스+1부터 비교를 해나간다.
# 만약 계속 같고 그렇게 비교를 해서 S의 끝에 도달하면 끝
# 만약 다르면 다음 k부터 다시 비교 시작

else:
    for k in start:
        if rS[:len(S)-k] == S[k:]:
            print(k+len(S))
            break
        else:
            continue

# sol2
i=len(S:=input())
while S!=S[::-1]:
    N,*S=S
    i+=1
print(i)

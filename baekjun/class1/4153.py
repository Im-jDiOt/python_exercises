# sol1 : function, list comprehension
def right(case: str) -> str:
    sides = sorted([int(side)**2 for side in case.split()])
    if sides[0] + sides[1] == sides[2]: print('right')
    else: print('wrong')

while (case := input()) != '0 0 0':
    right(case)
    
# sol2(other's) : without function, do-while
while True:
    a=list(map(int,input().split()))
    a.sort()
    if(a[0]==0 and a[1] ==0 and a[2]==0):break
    if(a[0]**2+a[1]**2==a[2]**2):
        print("right")
    else:
        print("wrong")
        
# do-while vs while
# https://stackoverflow.com/questions/390481/is-while-true-with-break-bad-programming-practice
# https://www.reddit.com/r/learnpython/comments/zbhw84/is_using_while_true_loops_good/
# 영어가 너무 많아서 그냥 대충 읽었는데 그냥 프로그래머 성향차인 거 같다. (2번째 reddit 베댓)
# 대신 break해야할 조건이 2개 이상인 경우엔 do-while을 쓰는 게 더 나은 거 같고 그 외의 server 등에서도 do-while을 주로 쓴다고 한다.

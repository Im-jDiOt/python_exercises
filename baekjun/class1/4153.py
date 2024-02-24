# sol1 : function, list comprehension
def right(case: str) -> str:
    sides = sorted([int(side)**2 for side in case.split()])
    if sides[0] + sides[1] == sides[2]: print('right')
    else: print('wrong')

while (case := input()) != '0 0 0':
    right(case)
    
# sol2(other's) : without function, do-while
while True:
    sides = list(map(int,input().split()))
    sides.sort()
    if(sides[0]==0 and sides[1] ==0 and sides[2]==0):break
    if(sides[0]**2+sides[1]**2==sides[2]**2):
        print("right")
    else:
        print("wrong")
        
# do-while vs while
# https://stackoverflow.com/questions/390481/is-while-true-with-break-bad-programming-practice
# https://www.reddit.com/r/learnpython/comments/zbhw84/is_using_while_true_loops_good/
# 영어가 너무 많아서 그냥 대충 읽었는데 그냥 프로그래머 성향차인 거 같다. (2번째 reddit 베댓)
# 대신 break해야할 조건이 2개 이상인 경우엔 do-while을 쓰는 게 더 나은 거 같고 그 외의 server 등에서도 do-while을 주로 쓴다고 한다.

# sol3 : better version of sol2
while (case := input()) != '0 0 0':
    sides = sorted(map(int, case.split()))
    if(sides[0]**2+sides[1]**2==sides[2]**2):
        print("right")
    else:
        print("wrong")

# 사실 넣을 생각 없었는데 commit msg에 3 solns라 적는 바람에... commit msg만 수정하는 법을 몰라 걍 무식하게 sol을 추가함.
# do-while에서 while로 바꿈. -> 종료 조건이 명확해져 가독성이 좋아짐.
# map 자체도 iterable하고 index 참조가 되는 자료형이기에 굳이 list로 형변환 하지 않아도 됨
# <iterable>.sort()는 오직 list만을 받기에 sorted()로 정렬해줌

# sort() vs sorted()
# 기능상 공/차 : 둘 다 정렬을 한다는 점에서 공통적임, 그러나 sort()는 list만을 받으며 받은 list를 정렬 후 None을 반환, sorted()는 iterable한 모든 자료형을 받으며 받은 iterable 자체를 정렬하여 반환.
# sort()의 장점 : original list가 필요하지 않을 경우 좀 더 효과적
# sorted()의 장점 : 대개 sort()보다 편리함. list 외의 다른 iterable한 것들을 받을 수 있음.
# https://docs.python.org/3/howto/sorting.html#sortinghowto

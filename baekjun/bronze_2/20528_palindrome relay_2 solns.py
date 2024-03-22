# sol1
import sys

N = int(input())
strings = input().split()
c = strings[0][0]

for string in strings:
    if string[0] == c:
        pass
    else:
        print(0)
        sys.exit()

print(1)

# sol2 (other's)
input()
print(1 if len({(s[0],s[-1]) for s in input().split()}) == 1 else 0)

# sol3
print(+(len({i[0]for i in[*open(0)][1].split()})==1))

# print(+True) -> 1, print(+False) -> 0
# open(0)도 input()이랑 비슷한 애인 거 같은데 내 vsc에서는 작동을 안 함......
# 근데 내가 알기로+방금 구글링한 결과 {}은 dictionary 선언할 때 쓰이지 set 선언할 때는 set()로 해야할텐데 어떻게 된 거지..?


# 겹치는 수들 -> set() 이용할 생각하자!!

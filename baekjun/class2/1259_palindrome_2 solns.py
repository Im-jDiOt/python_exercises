# sol1
while (case:=input()) != '0':
    if len(case) == 1: print('yes')
    elif len(case) == 2:
        if case[0] == case[1]: print('yes')
        else: print('no')
    elif len(case) == 3:
        if case[0] == case[2]: print('yes')
        else: print('no')
    elif len(case) == 4:
        if (case[0] == case[3]) and (case[1] == case[2]): print('yes')
        else: print('no')
    else:
        if (case[0] == case[4]) and (case[1] == case[3]): print('yes')
        else: print('no')

# sol2(other's) : [::-1]
import sys
while 1:
  n = sys.stdin.readline()[:-1]
  if n =='0':
    break

  if n == n[::-1]:
    print('yes')
  else:
    print('no')

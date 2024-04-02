# sol1 
while (line:=input()) != '#':
    cnt = 0
    for c in [65, 69, 73, 79, 85]:
        cnt += line.count(chr(c))
        cnt += line.count(chr(c+32))
    print(cnt)

# line = input().lower()로 하면 대소문자 다 따로 안 찾아줘도 된다.

# sol2(other's)
while 1:
  a=input()
  if a=='#': break
  else: print(sum(map(a.count,"aeiouAEIOU")))
  
# map을 이렇게 사용하다니!

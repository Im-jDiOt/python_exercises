# sol1
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
k = 1

wasOdd = a[0] % 2

for ai in a:
  if ai%2 != wasOdd:
    k += 1
    wasOdd = ai%2
  else:
    continue

print(k)

# sol2(other's)
n,*a=map(int,open(0).read().split())
i = -1
c = 0

for x in a:
 if(k:=x%2)!=i:
   c+=1
   i=k
   
print(c)

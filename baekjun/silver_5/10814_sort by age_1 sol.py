import sys
input = sys.stdin.readline
member = []

N = int(input())

for _ in range(N):
    member.append(input().split())

smember = sorted(member, key=lambda x:int(x[0]))

for i in range(N):
   print(smember[i][0], smember[i][1])


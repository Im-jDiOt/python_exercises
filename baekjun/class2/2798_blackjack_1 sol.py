# try1 -> runtime error
N, M = map(int, input().split())
cards =list(map(int, input().split()))
sums = set()

for i in range(N-2):
	for j in range(i+1,N-1):
		for k in range(j+1, N):
			sums.add(cards[i]+cards[j]+cards[k])
	
sums = sorted(sums)

i = 0
while sums[i] <= M:
	i += 1
	
print(sums[i-1])

# sol1
N, M = map(int, input().split())
cards = sorted(map(int, input().split()))
sums = set()

for i in range(N - 2):
  for j in range(i + 1, N - 1):
    for k in range(j + 1, N):
      sum = cards[i] + cards[j] + cards[k]
      if sum <= M:
        sums.add(sum)
      else:
        break

sums = sorted(sums)
print(sums[len(sums) - 1])

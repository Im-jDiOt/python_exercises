# sol1
T = int(input())
for _ in range(T):
  k, n = int(input()), int(input())
  residents = list(range(1, n+1))
  for _ in range(k):
    for i in range(1, n):
      residents[i] = residents[i] + residents[i-1]
  print(residents[n-1])

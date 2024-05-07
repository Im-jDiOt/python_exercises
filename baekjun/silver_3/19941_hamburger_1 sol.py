N, K = map(int, input().split())
hp = ['X' for _ in range(K)]+list(input())+ ['X' for _ in range(K)]
cnt = 0

for i in range(N+2*K):
  opponent = 0
  people = []
  
  if hp[i] == 'H':
    for j in range(1, K+1):
      if hp[i-j] == 'P':
        opponent += 1
        people.append(i-j)
      elif hp[i+j] == 'P':
        opponent += 1
        people.append(i+j)
      else:
        continue  
    if opponent == 1:
      cnt += 1
      hp[people[0]] = 'X'
    elif opponent >= 2:
      cnt += 1
      hp[sorted(people)[0]] = 'X'
    else:
      continue

print(cnt)

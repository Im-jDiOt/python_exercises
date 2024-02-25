# sol1 : take all numbers under num(inputed) as a divisor
N, nums = int(input()), map(int, input().split())
cnt = 0

for _ in range(N):
    num = next(nums)
    is_prime = True
    
    if num == 1: continue
    for divisor in range(2, num):
        if num % divisor:
            continue
        else:
            is_prime = False
            break
            
    if is_prime: cnt += 1
    else: continue
             
print(cnt)

# sol2 (will be added.. soooon... )

# sol1
S = input()
alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
res = []

for char in alphabet:
    if char in S:
        res.append(S.find(char))
    else:
        res.append(-1)
        
print(*res)

# sol2 : I found that I don't need res list after submit the code above..
S = input()
alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for char in alphabet:
    if char in S:
        print(S.find(char), end=' ')
    else:
        print(-1, end=' ')
        
# sol3(other's) : chr(i)
S = input()
for i in range(97,123):
    print(S.find(chr(i)), end=' ')
        
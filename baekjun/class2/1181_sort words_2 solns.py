# sol1
N = int(input())
words = set()

for _ in range(N):
    word = input()
    words.add((len(word), word))
    
sorted_words = sorted(words, key=lambda x: (x[0], x[1]))

for x, y in sorted_words:
    print(y)

# sol2(other's+edited by me)
import sys
N = int(input())

words = set(sys.stdin.readline().strip() for _ in range(N))
words = sorted(words)
result = sorted(words, key = lambda x:(len(x)))

print("\n".join(result))

# sorted()는 iterable을 받아 sorting한 리스트로 반환해준다.
# 이 때 sorting의 기준을 key로 지정해줄 수 있으며, tuple형태로 여러 개의 기준을 줄 수 있다. 
# 하나의 sorted()+여러 개의 key vs 여러 개의 sorted() --> 뭐가 더 빠를까?

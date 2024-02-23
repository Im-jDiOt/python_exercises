# sol1 : split()
words = input().split()
print(len(words))

# sol2 : slicing
words = input()
print(words[1:len(words)-1].count(' ')+1 if words != ' ' else 0)

# sol3(other's) : strip
words = input()
print(words.strip(' ').count(' ') + 1 if words != ' ' else 0)

# sol2 처음에 ' ' 예외 조건 설정 안해서 틀렸었다. 

R, C = map(int, input().split())
A, B = map(int, input().split())
mark = ['X', '.']

for j in range(R):
    for _ in range(A):
        for i in range(C):
            print(mark[i%2-j%2]*B, end='')
        print()

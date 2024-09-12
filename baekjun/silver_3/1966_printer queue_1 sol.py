import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    importance = list(map(int, input().split()))
    doc = list(enumerate(map(int, importance)))

    m = max(importance)
    ans = []

    while doc:
        for d, i in doc[:]:
            if i < m:
                continue
            else:
                importance.remove(m)
                doc.remove((d,i))
                ans.append(d)

                if importance: m = max(importance)
                else: pass
            

    print(ans.index(M)+1)


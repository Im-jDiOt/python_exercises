i = 0
while (n:=int(input())):
    i += 1
    not_same = True
    while not_same:
        li_n = list(map(int, list(str(n))))
        m = []
        if len(li_n)%2:
            print(f'Test {i}: {n}')
            break
        else:
            for x in range(int(len(li_n)/2)):
                m.append(li_n[2*x]*str(li_n[2*x+1]))
            if ''.join(m) == str(n):
                not_same = False
                print(f"Test {i}: {''.join(m)}")
            else: n = int(''.join(m))

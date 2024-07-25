import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 그냥 N개의 1을 가능할 때까지 빼기
    N, K = map(int, input().split())
    RUN_num_list = []
    
    while K:
        run = K // int(''.join(['1' for _ in range(N)]))
        
        if run:
            RUN_num = run*int(''.join(['1' for _ in range(N)]))            
        else:
            RUN_num = 9*int(''.join(['1' for _ in range(N-1)]))
                   
        RUN_num_list.append(RUN_num)
        K -= RUN_num
        N = len(str(K))

    print(len(RUN_num_list))
    print(*RUN_num_list)

    # 10 
    # 11 x
    # 110
    # 111 x
    # 이런 식으로 111이 안 들어갈 경우
    # 21도 결국엔 11 10 으로 되니까
    # 아무튼 그래서 11...1 이 안 들어가는 경우
    # 그러면 그 N-1개의 9..9 를 넣어줘야 함.

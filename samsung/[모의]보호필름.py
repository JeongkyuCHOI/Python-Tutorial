import sys
sys.stdin = open("sample_input (보호필름).txt", "r")

''' 
def 세로 검사
1) for문을 돌리면서 원소와 다음원소가 같으면 스택을 1추가
2) 같지않으면 스택을 0으로 초기화
3) 스택이 합격기준을 통과하면 다음 열로 넘어감
4) 모두 충족시 True
'''
def check(film, K):
    is_pass = [False for _ in range(W)]
    for x in range(W):
        stack = 0
        for y in range(D-1):
            if film[y][x] == film[y+1][x]:
                stack += 1
            else:
                stack = 0

            if stack == K-1:
                is_pass[x] = True
                break

    if False in is_pass:
        return False
    else:
        return True

'''
def dfs
1) 약품을 바르는 횟수를 depth 로 갖는 dfs
2) 재귀가 종료되면 약품바른 후 상태를 초기화해야함 
- 전체 deepcopy 대신 약품을 바른 줄의 상태만 복사해놓고 초기화하기
- 깊이가 기존 최소값보다 깊어지면 바로 리턴 
'''
def dfs(cnt, depth, film):
    global result

    # 현재의 최소값 보다 더 약품을 주입할 경우 리턴
    if cnt >= result:
        return

    # 약품 주입으로 완성되었는지 체크
    if check(film, K):
        # 최소값일 경우 업데이트
        if cnt < result:
            result = cnt
        return

    # 약품 주입횟수가 기준 횟수까지 도달하면
    if cnt == K:
        # 최소값일 경우 업데이트
        if cnt < result:
            result = cnt
        return

    else:
        # 약물 주입 경우의수. 약물 주입위치 depth, 최대 D
        for y in range(depth, D):
            switched = []
            for x in range(W):
                if film[y][x] == 1:
                    film[y][x] = 0
                    switched.append(x)
            dfs(cnt+1, y+1, film) # 약품 주입후의 경우의수 탐색
            for x in switched:
                film[y][x] = 1 # 원래 상태로 복원

            switched = []
            for x in range(W):
                if film[y][x] == 0:
                    film[y][x] = 1
                    switched.append(x)
            dfs(cnt+1, y+1, film)
            for x in switched:
                film[y][x] = 0

T = int(input())
for test_case in range(1, T+1):
    D, W, K = list(map(int, input().split()))
    if K == 1:
        result = 0
    else:
        result = 14 # D의 최대값+1
        film = [list(map(int, input().split())) for _ in range(D)]
        dfs(0,0,film)

    print("#{} {}".format(test_case, result))

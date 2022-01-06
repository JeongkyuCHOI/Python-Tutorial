import sys
sys.stdin = open("sample_input (1).txt", "r") # 테스트용
'''
조건1) 대각사각형 모양으로 방문하되 돌아와야함 => dfs 하되 불가능한 경로면 return
조건2) 재방문 x => Visited 쓰기 
조건3) 디저트 종류 같은곳 방문 x => 조건문에 값 확인 추가 

출력)가장 많은 디저트를 먹는 경우를 출력 => global 변수와 max 함수 이용 

1. 대각사각형 경로를 탐색하는 코드를 구성
2. DFS로 위 조건 구현
3. rotation 함수를 작성해서 총 4가지 경우를 검색

↖0 1↗
↙2 3↘   
d[y,x] = [0:[-1,-1], 1:[-1,1], 
          2:[ 1,-1], 3:[ 1,1]]
'''
d = [[-1,-1], [-1, 1], [1, -1], [1,1]]

def dfs(y, x, start_y, start_x, line):
    # 범위가 넘어감
    if x < 0 or x >=N or y < 0  or y >= N:
        return

    # 방향 3번 바꾸었고 시작점과 도착점이 같음
    if line == 3 and y == start_y and x == start_x:
        sel.append(len(visited))
        return

    # 현재 디저트
    cur = board[y][x]
    # 방문한적 있음
    if cur in visited:
        return

    # 방향 바뀐 횟수가 4번이상
    if line >= 4:
        return

    # 진행하기
    visited.add(cur)
    dfs(y+d[line][0], x+d[line][1], start_y, start_x, line)
    visited.remove(cur)

    # 방향꺾기
    if line < 3:
        visited.add(cur)
        dfs(y+d[line+1][0], x+d[line][1], start_y, start_x, line+1)
        visited.remove(cur)



    # 방향 전환
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    sel = []
    for y in range(N):
        for x in range(N):
            visited = set()
            dfs(y=y, x=x, start_y=y, start_x=x, line=0)
    result = max(sel) if sel else -1
    print('#{} {}'.format(test_case, result))
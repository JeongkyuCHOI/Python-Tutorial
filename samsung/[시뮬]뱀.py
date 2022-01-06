n = int(input()) 
k = int(input())
board = [[0]*n for _ in range(n)]

apples = [list(map(int, input().split())) for _ in range(k)]
for y, x in apples:
    board[y-1][x-1] = 1
L = int(input())
turns = [input().split() for _ in range(L)]

'''
1.뱀이 존재하는 곳의 좌표를 원소로 갖는 리스트 생성
2.이동 시 뱀의 좌표 업데이트
3.이동 시 조건에 해당하는지 확인 
'''
snake =[[0,0]]
sec = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#   상U 하D 좌L 우R

def dir(cur, nxt):
    if nxt == 'L':
        if cur == 'L':
            return 'D'
        elif cur =='R':
            return 'U'
        elif cur =='U':
            return 'L'
        else: # cur =='D'
            return 'R'

    else: #nxt == 'D'
        if cur == 'L':
            return 'U'
        elif cur =='R':
            return 'D'
        elif cur =='U':
            return 'R'
        else: # cur =='D'
            return 'L'
def move(board):
    global sec
    global snake
    direction = 'R'
    idxy = 0
    while True:
        # 이동조건 
        # 1)방향체크
        if direction =='L':   idxy = 2
        elif direction =='R':  idxy = 3
        elif direction =='D':  idxy = 1
        else:  idxy = 0

        # 2)전진
        sec += 1 # 1초 증가
        y, x = snake[-1] # y,x 원래위치
        next_y = y + dy[idxy] # next_y, x 다음위치 
        next_x = x + dx[idxy]
        # 종료조건 : 벽이나 몸에 부딫힘 
        if next_y < 0 or next_x < 0 or next_y >= n or next_x >= n: 
            return

        if [next_y, next_x] in snake:
            return

        # 3)사과체크 
        if board[next_y][next_x] != 1:
            if len(snake) >= 1:
                snake = snake[1:]
            # 사과안먹으면 꼬리가 줄어줌
        else:
            board[next_y][next_x] = 0
        snake.append([next_y, next_x]) # 다음위치로 머리 이동 
        
        # 4)방향 변환체크
        for turn in turns:
            if turn[0] == str(sec):
                # direction = turn[1]
                direction = dir(direction, turn[1]) 


move(board)
print(sec)
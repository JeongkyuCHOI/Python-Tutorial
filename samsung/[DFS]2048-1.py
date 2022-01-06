n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

'''
- 각 방향 이동을 회전 + 이동으로 나누어 생각
  > 각 방향 회전 함수 Rotate() : 시계방향으로 90도 회전
  > 이동 함수 Move() : 왼쪽 방향으로 이동
- 최대 이동회수가 정해져있으므로 depth가 한정적인 경우 모든 경우를 탐색할때
  용이한 dfs를 사용하자 
'''

from copy import deepcopy 
# 시계방향 90도 회전
def rotate(board):
    n = len(board) # 세로길이, 행, y
    m = len(board[0]) # 가로길이, 열, x 

    new_board = deepcopy(board)
    for i in range(n): 
        for j in range(m):
            # new_board[i][j] = board[n-1-j][i]
            new_board[j][n-1-i] = board[i][j]

    return new_board

# << 이쪽으로 더하기
def move(board_rows):
    # 1. 값이 있는 부분만 고려 (0인 부분은 고려 x)
    temp_lst = [i for i in board_rows if i != 0]

    # 2. temp_lst에서 같은 값이 겹치는지 확인
    for i in range(1, len(temp_lst)):
        if temp_lst[i-1] == temp_lst[i]:
            temp_lst[i-1] *= 2 # 합치기
            temp_lst[i] = 0 # 0 만들기

    # 3. 합쳐진 다음 다시 원래 길이로 붙이기
    # 왼쪽으로 붙이기
    answer_lst = [i for i in temp_lst if i != 0]  
    # 원래 길이로 복원
    zero_len = len(board_rows) - len(answer_lst)
    # print('zero_len', zero_len)

    if zero_len != 0: # 합쳐진 경우에만 복원
        for _ in range(zero_len):
            answer_lst.append(0) 
     

    global max_val 
    # print('temp_lst', answer_lst)
    # is_max = [max(i, max_val) for i in answer_lst] 
    max_val = max(max_val, max(answer_lst))
    # print('max_val', max_val)

    return answer_lst

# 
max_val = 0

def dfs(depth, board):
    # 종료 조건
    if depth == 5: 
        return
        
    # 반복 조건 
    # depth+1 씩 탐색
    for _ in range(4):
        board = rotate(board)
        # move 함수는 <<이쪽 연산을 하므로 행단위로 넣기
        new_board = []
        for row in board:
            line = move(row)
            new_board.append(line)
        # print('new_board\n', new_board)
        dfs(depth+1, new_board)
        

dfs(0, board)
print(max_val)
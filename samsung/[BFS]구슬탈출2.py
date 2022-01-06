n, m = list(map(int, input().split()))
table =[]
for _ in range(n):
    line = list(input())
    table.append(line)

# print('table:\n', table)
# n, m = 7, 7 
# table = [['#', '#', '#', '#', '#', '#', '#'], 
#          ['#', '.', '.', '.', 'R', 'B', '#'], 
#          ['#', '.', '#', '#', '#', '#', '#'], 
#          ['#', '.', '.', '.', '.', '.', '#'], 
#          ['#', '#', '#', '#', '#', '.', '#'], 
#          ['#', 'O', '.', '.', '.', '.', '#'], 
#          ['#', '#', '#', '#', '#', '#', '#']]

'''
8 8
########
#.####.#
#...#B##
#.##.R.#
######.#
##.##O.#
###.##.#
########
# ANS:7

4 6
######
#R####
#B..O#
######
ANS:-1

4 6
######
#R#O##
#B...#
######
ANS:4

'''
r_x, r_y, b_x, b_y = 0, 0, 0, 0
for y in range(n):
    for x in range(m):
        if table[y][x]=='R':
            r_x, r_y = x, y
        elif table[y][x]=='B':
            b_x, b_y = x, y

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상U 하D 좌L 우R
from collections import deque
min_count = 11
def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 0))
    visited = []
    visited.append((rx, ry, bx, by))
  
    global min_count 
    while queue:
        # print(queue)
        x_r, y_r, x_b, y_b, cnt = queue.popleft()
        if cnt > 10:
            return
        if table[y_r][x_r] == 'O':
            min_count = min(min_count, cnt)
            continue 
        
        for i in range(4): # 0:U 1:D 2:L 3:R 
            nx_r, ny_r = x_r, y_r 
            while True:
                nx_r += dx[i]
                ny_r += dy[i] 
                if table[ny_r][nx_r] == '#':
                    nx_r -= dx[i] 
                    ny_r -= dy[i]
                    break
                if table[ny_r][nx_r] == 'O':
                    break

            nx_b, ny_b = x_b, y_b
            while True:
                nx_b += dx[i]
                ny_b += dy[i]
                if table[ny_b][nx_b] =='#':
                    nx_b -= dx[i]
                    ny_b -= dy[i]
                    break
                if table[ny_b][nx_b] == 'O':
                    break
                
            if table[ny_b][nx_b] == 'O':
                continue
            
            if nx_r == nx_b and ny_r == ny_b:
                dis_r = abs(nx_r - x_r) + abs(ny_r - y_r)
                dis_b = abs(nx_b - x_b) + abs(ny_b - y_b)
                
                if dis_r > dis_b:
                    nx_r -= dx[i]
                    ny_r -= dy[i]
                    
                else:
                    nx_b -= dx[i] 
                    ny_b -= dy[i]
            
            if (nx_r, ny_r, nx_b, ny_b) not in visited:
                queue.append((nx_r, ny_r, nx_b, ny_b, cnt+1))
                visited.append((nx_r, ny_r, nx_b, ny_b))
    return

bfs(r_x, r_y, b_x, b_y)
if min_count == 11:
    print(-1)
else:
    print(min_count)



    
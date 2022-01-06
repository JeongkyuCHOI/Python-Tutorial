import time
## 4-1, 111p, 상하좌우
def UDRL():
    try:
        N  = int(input('Enter the size N (1<= N <=100)\n'))
        MAP = list(map(str, input('Enter the map for moving\n').split()))
        # map은 리스트의 요소를 첫번째 인자(함수)로 처리
    except:
        print('Check the rules of these values')
        return


    if not (1 <= N <= 100) :
        print("N should follow the rule")
        return

    rows, cols = N, N
    num_map = len(MAP)

    x, y = [1, 1]

    for step in MAP:
        if step=='U':
            if x == 1:
                continue
            else:
                x = x - 1

        elif step=='D':
            if x == cols :
                continue
            else:
                x = x +1

        elif step=='R':
            if y == rows:
                continue
            else:
                y = y + 1

        elif step=='L':
            if y == 1:
                continue
            else:
                y = y - 1

        else:
            print('Only U, D, R, L are valid')
            return

    print('Result is %d %d'%(x, y))

## 4-2, 113p, 00시 00분 00초부터 N시 59분 59초까지 3이 포함되는 갯수 찾기
def TIME():
    try:
        N = int(input("Enter the time 'N'(0<=N<=23)\n"))
    except:
        print('Check the rules of these values')
        return

    minutes = list(range(0, 60))
    seconds = list(range(0, 60))
    hours = list(range(0, N+1))
    candidates = [3, 13, 23, 43, 53, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    count = 0
    start_time = time.time()
    for hour in hours:
        for minute in minutes:
            for second in seconds:
                if second in candidates:
                    count = count +1
                elif minute in candidates:
                    count = count +1
                elif hour in candidates:
                    count = count+1
                else:
                    continue

    print('The processing time is %.4f seconds'%(time.time()-start_time))
    print('The number of the cases :', count)


def Knight():
    try:
        x, y = map(str, list(input("Entehr the cordinate of x, y(a~h, 1~8)\n")))
        x = ord(x) -96 # 아스키코드 'a'= 97
        y=int(y)

    except:
        print('Check the range')
        return

    r_space = 8 - x
    l_space = x - 1
    u_space = y - 1
    d_space = 8 - y

    count = 0
    if (r_space >= 2) and (u_space >= 1):
        count = count + 1
    if (r_space >= 2) and (d_space >= 1):
        count = count + 1
    if (l_space >= 2) and (u_space >= 1):
        count = count + 1
    if (l_space >= 2) and (d_space >= 1):
        count = count + 1
    if (u_space >= 2) and (r_space >= 1):
        count = count + 1
    if (u_space >= 2) and (l_space >= 1):
        count = count + 1
    if (d_space >= 2) and (r_space >= 1):
        count = count + 1
    if (d_space >= 2) and (l_space >= 1):
        count = count + 1

    print("Reuslt is %01d"%count)

def mapGame():
    try:
        N, M = list(map(int, input('Enter the height(N), width(M) of map size in the range(1<=N<=4, 1<=m<=50)\n').split()))
        A, B, d = list(map(int, input('Enter the initial position(y, x) and dirention(d)\nThe reference point is the upper left corner\n').split()))
        print("%d %d         N M\n%d %d %d       A B d" % (N, M, A, B, d))
    except:
        print('Check the range of those values')
        return
    if not ((1<=N<=4) and (1<=M<=50) and (0<=A < N) and (0<=B < M) and (0<= d <=3)):
        print('Check the range of those values')
        return

    print("Enter the [1 or 0] at each position")
    mymap=list()
    for _ in range(N):
        row = list(map(int, input().split()))
        if not (1 in row) and (0 in row):
            print('Only [1] , [0] are allowed')
            return
        mymap.append(row)

    dx = B # 초기 위치에서 얼마만큼 x방향으로 이동
    dy = A # 초기 위치에서 얼마만큼 y방향으로 이동

    count=0
    if mymap[dy][dx] == 0:
        count = count +1
    while True:
        if d == 3:
            if (dy-1) >=0 :
                dy = dy -1 # y축 위로 진행
                if mymap[dy][dx] == 0:
                    count = count +1 # 이동횟수 +1
                    mymap[dy][dx] = 1 # 가본곳 체크
                    d=0
                else:
                    dy = dy +1 # 막혔으므로 y축 다시 아래로
                    d = 0 # 회전 3>0
            else :
                d=0
        if d == 0:
            if (dx-1) >=0 :
                dx = dx -1 # x축 왼쪽 진행
                if mymap[dy][dx] == 0:
                    count = count +1
                    mymap[dy][dx] = 1 # 가본곳 체크
                    d=1
                else:
                    dx = dx + 1
                    d = 1
            else:
                d=1
        if d == 1:
            if (dy+1) <= N:
                dy = dy +1
                if mymap[dy][dx] ==0:
                    count = count+1
                    mymap[dy][dx] = 1 # 가본곳 체크
                    d=2
                else:
                    dy = dy -1
                    d = 2
            else:
                d=2
        if d == 2:
            if (dx+1) <= M:
                dx = dx +1
                if mymap[dy][dx]==0:
                    count = count+1
                    mymap[dy][dx] = 1 # 가본곳 체크
                    d=3
                else:
                    dx = dx-1
                    d = 3
            else:
                d=3

        if ((mymap[dy-1][dx] == 1) and
            (mymap[dy][dx-1]==1 ) and
            (mymap[dy+1][dx]==1) and
            (mymap[dy][dx+1]==1)) == True:
            print(count)
            break



if __name__=="__main__":
    # UDRL()
    # TIME()
    # Knight()
    mapGame()







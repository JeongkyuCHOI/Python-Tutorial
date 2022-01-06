# 7. 럭키스트레이트
def lucky_straight():
    n = int(input())
    n = list(map(str, str(n)))
    
    n_len = len(n)
    left = range(0, n_len//2)
    right = range(n_len//2, n_len)
    left_sum = 0
    right_sum = 0
    for left_idx in left:
        left_sum += int(n[left_idx])

    for right_idx in right:
        right_sum += int(n[right_idx])

    if left_sum == right_sum:
        print('LUCKY')
    else:
        print('READY')
    
# 8. 문자열 재정렬
def re_arrange():
    data = input()

    numbers_set = list(map(str, range(0,10)))

    result =[]
    alphabet =[]
    numbers =[]
    for dat in data:
        if not dat in numbers_set:
            alphabet.append(dat)
        else:
            numbers.append(dat)
    alphabet.sort()
    sum = 0
    for num in numbers:
        sum += int(num)

    alphabet.append(str(sum))

    result = alphabet
    for i in range(len(result)):
        print(result[i], end='')

# 9. 문자열 압축
'''
def solution(s):
    s_len = len(s)
    if s_len == 1: return 1
    
    half = len(s)//2 
    best = 1000


    for n in range(1, half):
        temp=[]

        if not n == 1:
            mini_s = [s[i:i+n] for i in range(0, len(s), n)]
        else:
            mini_s = s 
        num = 0
        print(n, ' 잘려진 리스트: ', mini_s)
        for i, ss in enumerate(mini_s):
            if i == 0:
                continue
            else:
                if not len(ss) == len(mini_s[0]):
                    temp.append(ss)
                print(i-1, i)
                if s[i-1] == s[i]:
                    num += 1
                else:
                    if not num == 1:
                        print(str(num), ss)
                        temp.append(str(num)+ss)
                        num = 0
                    else:
                        temp.append(ss)
        result = len(temp)
        print('temp', temp)
        if result < best:
            best = result
    answer = best
    print(answer)
    return answer
'''
def solution(s):
    answer = len(s)

    # 길이의 반만큼만 확인하면 됨
    for i in range(1, int(len(s)/2)+1):
        pos = 0
        length = len(s)

        # i만큼 다음문자열 읽어와서 확인
        while pos + i <= len(s): 
            unit = s[pos:pos+i] #압축하고자하는 문자열 읽어옴  
            pos += i # 포지션 진행

            cnt = 0
            while pos + i <= len(s):
                if unit == s[pos:pos+i]:
                    cnt += 1
                    pos += i
                else:
                    break

            if cnt > 0: # 반복된 count가 있으면
                length -= i * cnt

                if cnt < 9:
                    # 반복되는 수가 9보다 작으면 
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4

        answer =min(answer, length)

    return answer

# 10. 자물쇠와 열쇠
# https://www.youtube.com/watch?v=RrWnBaflV2o
def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0: 
                arr[r + i][c + j] += key[i][j] # 겹친 부분 표시하기위해 더함
            elif rot == 1: # 90도 회전
                arr[r + i][c + j] += key[n-1-j][i]
            elif rot == 2: # 180도 회전
                arr[r + i][c + j] += key[n-1-i][n-1-j]
            else: # 270도 (90도 반대로 회전이랑 같음)
                arr[r + i][c + j] += key[j][n-1-i]   

def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True

def solution(key, lock):
    
    offset = len(key) - 1 

    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for rot in range(4):
                # 큰 맵 생성
                arr = [[0 for _ in range(58)] for _ in range(58)]

                # 자물쇠 복사
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True

    return False

# 11. 뱀
def snake():
    n = int(input()) # 맵의 크기 N x N
    k = int(input()) # 사과의 갯수 K
    board = [[[0] for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        yx = list(map(int,input().split())) # y,x
        
        row_y, col_x = yx[0], yx[1]
        board[row_y][col_x] = 1 # 사과 위치

    L = int(input()) # 뱀의 방향 변환 횟수 L
    info_dict = {}
    for _ in range(L):
        td = list(map(str, input().split()))
        time, direction = int(td[0]), td[1]
        info_dict[time] = direction

    # 진행하기 
    size = n - 1
    pro_x = 0
    pro_y = 0
    sec = 0
    cnt_L = 0
    cnt_R = 0
    direc = 0 
    while(pro_x >= 0 or pro_x <= size or pro_y >=0 or pro_y <= size):
        sec += 1
        direc = cnt_R - cnt_L # 진행 방향체크 
        if direc < 0 : direc =
        if direc == 0: # 우
            pro_x += 1
        elif direc == 1: # 하
            pro_y += 1
        elif direc == 2
        if sec in info_dict.keys():
            if info_dict[sec] == 'D':
                direc += 1 
            else:
                direc -= 1


if __name__ == '__main__':
    # re_arrange() # K1KA5CB7
    # lucky_straight()
    # solution('aabbaccc')
    # solution([[0, 0, 0], 
    #           [1, 0, 0], 
    #           [0, 1, 1]], 
    #          [[1, 1, 1], 
    #           [1, 1, 0], 
    #           [1, 0, 1]])

    snake()
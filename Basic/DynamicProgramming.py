'''
다이나믹프로그래밍, 메모리를 적절히 사용하여 수행시간 효율성 향상시킴
-> 이미 계산된 결과는 별도의 메모리에 저장하여 다시 계산하지 않도록함
-> 최적부분구조 조건: 큰문제를 작은문제로 나눔 
-> 중복되는 부분문제: 동일한 작은 문제 반복적으로 수행
'''

# 탑다운 방식(재귀함수)
# 한번 계산된 결과를 Momoization 하기 위한 리스트 초기화
d = [0] * 101
def fibo(x):
    if x ==1 or x==2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# 바텀업 방식(반복문)p
d = [0] * 101
d[1] = 1
d[2] = 1
def fibo(x):
    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]
    return d[x]

def ant_soldier(n, k):
    dp = [0] * n # DP 테이블 초기화 
    # 다이나믹 프로그래밍진행
    dp[0] = k[0] 
    dp[1] = max(k[0], k[1])
    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + k[i])

    return d[n-1]

# 1만들기 문제
def one_maker():
    # a_i= i를 1로 만들기 위한 최소 연산횟수 
    # a_i = min(a_i-1, a_i/2, a_i/3, a_i/5) + 1
    
    # 정수 x 입력받기
    x = int(input())
    # dp 테이블 초기화
    d = [0] * 30001 # 1~30000

    # 다이나믹 프로그래밍 (바텀-업)
    for i in range(2, x+1):
        # 현재의 수에서 1을 빼는 경우(i-1)
        d[i] = d[i-1] + 1
        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 ==0:
            d[i] = min(d[i], d[i//2] + 1)
        # 현재의 수가 3으로 나누어 떨어지는 경우
        if i % 3 ==0:
            d[i] = min(d[i], d[i//3] + 1)
        # 현재의 수가 5로 나누어 떨어지는 경우
        if i % 5 ==0:
            d[i] = min(d[i], d[i//5] + 1)
    print(d[x])

def money():
    # a_i = 금액 i를 만들수 있는 최소한의 화폐 개수
    # k = 각 화폐의 단위
    # 점화식: 각 화폐 단위인 k를 하나씩 확인하며
    # a_i = min( ai, ai-k +1), 


    # 화폐 개수 n, 화폐의 합 m
    n, m = map(int, input().split())
    # 화폐 종류 
    array = []
    for _ in range(n):
        array.append(int(input()))

    # 한번 계산된 결과를 저장하기 위한 DP 테이블     
    d = [10001] * (m+1) 
    
    # 다이나믹 프로그래밍 (바텀업)
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m+1):
            if d[j - array[i]] != 10001: #(i-k)원을 만드는 방법이 존재할 경우
                d[j] = min(d[j], d[j-array[i]]+1)
    
    # 계산된 결과 출력
    if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
        print(-1)
    else:
        print(d[m])

def gold_mountain():
    # 테스트 케이스 입력
    for tc in range(int(input())):
        # 금광 정보 입력        
        n, m = map(int, input().split())
        array = list(map(int, input().split()))
        
        # 2차원 dp 테이블 초기화 
        dp = []
        index = 0
        for i in range(n):
            dp.append(array[index:index+m])
            index += m
        
        # 다이나믹 프로그래밍 진행 
        for j in range(1, m): #열 기준 확인
            for i in range(n):
                # 왼쪽 위에서 오는 경우
                if i == 0: left_up =0
                else: left_up = dp[i-1][j-1]

                # 왼쪽 아래에서 오는 경우
                if i == n -1: left_down =0
                else: left_down = dp[i+1][j-1]

                # 왼쪽에서 오는 경우
                left = dp[i][j-1]
                dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        
        result = 0
        for i in range(n): 
            result = max(result, dp[i][m-1])
        print(result)
        
# 가장 긴 증가하는 부분 수열 
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 0<=j<i에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
def batch_soldier():
    n= int(input())
    array = list(map(int, input().split()))
    # 순서를 뒤집어 '최장 증가 부분 수열'문제로 변환
    array.reverse()

    # dp 테이블 초기화
    dp = [1] * n

    # 가장 긴 증가하는 부분수열 알고리즘 수행
    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)
    # 열외해야하는 최소 병사수
    print(n-max(dp))

if __name__ == '__main__':
    # print(fibo(100))

    # n = int(input())
    # k = list(map(int,input().split()))
    # ant_soldier(n,k)

    # one_maker()
    # gold_mountain()
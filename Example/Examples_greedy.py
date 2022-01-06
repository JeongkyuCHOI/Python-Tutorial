# 1. 모험가길드
def guild_1(n, x):
    x.sort() 
    result = 0

    count = 0 # 그룹내 모험가수
    for i in x:
        count += 1
        if count >= i: #그룹내 모험가수가 공포도 보다 많으면
            result += 1
            count = 0
    return result

# 2. 곱하기 혹은 더하기
def maximum_2(s):
    s = list(map(int, s))
    result = s[0]
    for i in range(1, len(s)):
        if s[i] <= 1 or result <= 1:
            result += s[i]
        else:
            result *= s[i]
    return result


# 3. 문자열 뒤집기
def flip_str():
    data = input()

    count0 = 0 # 모두 0인 경우
    count1 = 0 # 모두 1인 경우
    
    # 첫번째 원소 처리
    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1
    
    # 두번째 원소부터 모든 원소 확인
    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            # 다음 수에서 1로 바뀌는 경우(0으로 세팅)
            if data[i +1]== '1':
                count0 += 1
            # 다음 수에서 0으로 바뀌는 경우(1로 세팅)
            else:
                count1 += 1
    print(min(count0, count1))            

# 4. 만들 수 없는 금액 
def convinience():
    # n=5, 3 2 1 1 9 => 8 8//1 -0 8//2 -0 8
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    
    target = 1 
    for x in coins:
        # 만들 수 없는 금액을 찾았을때 반복 종료
        if target < x:
            break
        target += x 
    print(target)

# 5. 볼링공 고르기
import time
def balling():
    # 볼링공 N개, 볼링공의 무게 1~M까지
    # 서로다른 무게의 볼링공을 고르는경우의 수
    N, M = list(map(int, input().split()))
    balls = list(map(int, input().split()))

    start_time = time.time()
    balls.sort()

    count = 0 
    for i in range(N-1):
        for j in range(i+1, N):
            if balls[i] == balls[j]:
                continue
            else:
                count += 1
    print(count) 
    print('The processing time is %.4f seconds'%(time.time()-start_time))

    # 정답 : A가 특정 무게의 공 골랐을때 x 이어서 B가 특정 무게의 공 골랐을때 고려
    # 볼링공 무게의 범위 1~10까지 무게를 담을수 있는 리스트
    start_time = time.time()
    array = [0] * 11
    for x in balls:
        array[x] += 1 

    result = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, M+1):
        N = N - array[i] # 무게가 i인 공의 개수 제외 (A가 선택할 수 있는 개수)
        result = result + array[i] * N # B가 선택하는 경우의 수와 곱하기
    print(result)
    print('The processing time is %.4f seconds'%(time.time()-start_time))

from operator import itemgetter
def mukbang(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))

    foods.sort()

    pretime = 0
    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k][1]
        n -= 1
        
    return -1
   
if __name__=='__main__':
    # n = int(input())
    # x = list(map(int, input().split()))
    # print(guild_1(n,x))

    # s = list(map(str, input()))
    # print(maximum_2(s))

    # flip_str()
    # convinience()

    # balling()
    print(mukbang([3,1,2], 5))
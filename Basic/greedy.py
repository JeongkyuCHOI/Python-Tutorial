## 3-1, 87p. 거스름돈의 동전의 수를 최소화 => 큰돈부터 계산하기
def changes_1(N):
    if N % 10 != 0 :
        print('Input Money (N) is ', N)
        print('N have to a multiple of 10 !!')
        return
    '''
    coin_500 = N//500
    deducted_by_500 = N % 500

    coin_100 = deducted_by_500 //100
    deducted_by_500_100 = deducted_by_500 % 100

    coin_50 = deducted_by_500_100 // 50
    deducted_by_500_100_50 = deducted_by_500_100 % 50

    coin_10 = deducted_by_500_100_50 // 10

    coins = coin_500 + coin_100 + coin_50 + coin_10
    print('The number of coins : %d' % coins )
    print('500: %d, 100: %d, 50: %d, 10: %d' %
          (coin_500, coin_100, coin_50, coin_10))
    '''
    coin_types = [500, 100, 50, 10]
    coins = 0
    for coin in coin_types:
        coins += N // coin
        N %= coin
    print('The number of coins : %d' % coins )

## 3-2, 큰수의 법칙
import sys
def big_num_2():
    # 배열의 크기N, 숫자가 더해지는 횟수 M, 하나의 인덱스가 최대중복더하기 횟수 K
    print("Enter the N, M, K values")
    N, M, K =map(int, input().split())
    # sys.stdin.readline().rstrip()

    if not ((2<= N <= 1000) and (1<= M <= 10000) and (1<= K <= 10000)) :
        print( "N, M, K have to follow the rule of range")
        return
    elif M < K :
        print("M should more than K")
        return
    print("Input N:%d, M:%d, K:%d" % (N,M,K))

    print("Enter N natural numbers")

    numbers = list(map(int, input().split()))
    print(numbers)
    if not len(numbers) == N :
        print('The length of natural numbers should equal N')
        return
    for number in numbers:
        if not 2 <= number <= 10000 :
            print('Natural numbers have to follow the rule of range')
            return

    numbers.sort(reverse=True) # 입력 숫자 내림차순 정리

    # 수열그려보고 규칙찾기
    num_numbers = M // (K+1) # 숫자가 더해지는 횟수 M을 최대 반복횟수 K로 나눈 몫
    num_numbers2 = M % (K+1) # 나머지
    result = num_numbers * ( numbers[0] * K + numbers[1] ) + num_numbers2 * numbers[0]

    print('The summation result is :', result)

## 3-3, 숫자 카드게임
import random
import numpy as np
def card_game_3():
    print("Enter the N, M values")
    N, M =map(int, input().split())
    if not (N >= 1) and ( M <= 100) :
        print( "N, M should follow the rule of range")
        return

    # array = [[random.randrange(1,10)] * M for _ in range(N)]
    array = np.random.randint(1,10001,(N,M))
    # print(array) # np array

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            print(str(array[i,j]), end=' ')
        print()


    array_sorted = np.sort(array, axis=1) #  열 기준 정렬
    array_list = []
    for i in range(array_sorted.shape[0]):
        array_list.append(array_sorted[i,0])
    array_list.sort()

    print('\nResult is %d'%array_list[-1])


## 3-4, 1이 될때까지
import time
def go_to_one():
    print("Enter the N, K values")
    N, K = map(int, input().split())
    if not (2<=N<=100000) and (2<=K<=100000) and (N>=K):
        print("N, K should follow the rule")
        return

    count =0
    while N!=1 :
        if N % K == 0:
            N = N/K
        else:
            N = N-1
        count = count + 1

    print("The minimum number of iterations is %d" % count)

if __name__=="__main__":
    # changes(1260) # 3-1
    # big_num_2()
    # card_game_3()
    go_to_one()

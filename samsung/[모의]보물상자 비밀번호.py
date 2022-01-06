import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())


'''
변의 길이는 N/4 
ex) N= 16이면 각 변은 16/4 = 4. Rotate는 변의길이-1= 3만큼하면 차이x 

1) 주어진 numbers 를 각 변의 길이로 잘라서 10진수로 만든 듬 
2) 만든 수들을 붙임
3) Rotate 한 경우를 append
4) 모든 경우를 내림차순(중복x) 정렬 
'''
from collections import OrderedDict

numbers_lst = []

def rotate(numbers):
    output_lst = numbers[-1]
    for i in range(len(numbers)-1):
        output_lst += numbers[i]

    # print('input', numbers)
    # print('output', output_lst)
    return output_lst

def BOX(numbers, N):
    global numbers_lst

    length = N // 4 # 한 변의 길이
    # N=16이면 한변의 길이는 16/4= 4, 4묶음
    # N=20이면 한변의 길이는 20/4=5,
    rotated_numbers = 0
    for rotate_cnt in range(N-1): # N-1번 회전 경우의 수 고려
        if rotate_cnt == 0:
            rotated_numbers = numbers
        else:
            rotated_numbers = rotate(rotated_numbers)
        # print('회전횟수', rotate_cnt)
        # print('회전숫자', rotated_numbers)
        for i in range(4): # 0 1 2 3 4
            start = length*i # 0, 6, 12, 18, 24
            end = length*(i+1) # 5, 10, 15, 20, 25
            # 0 1 2 3 4 / 5 6 7 8 9 / 10 11 12 13 14 / 15 16 17 18 19
            value = rotated_numbers[start : end] # 각 변의 숫자

            numbers_lst.append(value)
    # print('numbers_lst len', len(numbers_lst))
    # print('numbers_lst', numbers_lst)

def find_k(numbers, k):
    # string 으로 된 16진수 리스트 numbers
    answer_lst = []
    for number in numbers:
        number = int(number, 16) # 16진수(string) > 10진수(int)
        answer_lst.append(number)

    # result = list(OrderedDict.fromkeys(answer_lst).keys())
    result = list(set(answer_lst))
    result.sort(reverse=True)

    return result[k-1]

for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # 숫자갯수 N, 가장큰 K번째 수
    numbers = input()

    BOX(numbers, N)

    answer = find_k(numbers_lst, K)
    numbers_lst = []

    print('#%d %d'%(test_case,answer))



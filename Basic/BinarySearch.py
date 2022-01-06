'''
순차 탐색: 특정 데이터를 찾기위해 앞에서 부터 확인
이진 탐색 : 정렬되어 있는 리스트에서 범위를 절반씩 좁혀가며 탐색
=>단계마다 탐색 범위를 2로 나누므로 시간 복잡도 O(logN)
=>시작점, 끝점, 중간점을 이용해 탐색 범위 지정 
'''

# 이진 탐색 소스코드 구현 (재귀함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2 # 중간점
    
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)

# 이진 탐색 소스코드 구현 (반복문)
def binary_search_iter(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None

'''
정렬된 순서를 유지하면서 배열a에 x를 삽입할 위치 반환
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
     0  1  2  3  4 <-index 
x = 4
print(bisect_left(a,x)) = 2 
print(bisect_right(a,x)) = 4
'''
# 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

'''
파라메트릭 서치(Parametric search)
최적화 문제를 결정문제로 바꾸어 해결하는 기법
특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제, 이진탐색 이용 
'''
# 떡볶이 떡 만들기 문제
def dduck():
    # 떡의 개수(N)과 요청한 떡의 길이(M) 입력받음
    n, m = list(map(int, input().split()))
    # 각 떡의 개별 높이 정보를 입력
    array = list(map(int, input().split()))

    # 이진탐색을 위한 시작점과 끝점
    start = 0
    end = max(array)
    
    # 이진탐색 수행
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            # 잘랐을 때 떡의 양
            if x > mid:
                total += x-mid
        # 떡의 양이 부족하면 더 많이 자르기 : 왼쪽 탐색
        if total < m:
            end = mid - 1
        # 떡의 양이 많으면 더 적게 자르기 : 오른쪽 탐색
        else:
            result = mid
            start = mid + 1
    print(result)
    


if __name__=='__main__':
    '''
    # 원소의 개수 n과 찾고자 하는 값 target을 입력 받기 
    n, target = list(map(int, input().split()))
    # 전체 원소 입력받기
    array = list(map(int, input().split()))

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n-1)
    # result = binary_search_iter(array, target, 0, n-1)

    if result == None:
        print('원소가 존재하지 않습니다')
    else:
        print(result+1)
    '''

    '''
    a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9] # 배열 선언
    # 값이 4인 개수 출력 
    print(count_by_range(a, 4, 4))
    # 값이 [-1, 3]인 개수 출력
    print(count_by_range(a, -1, 3))
    '''

    dduck()
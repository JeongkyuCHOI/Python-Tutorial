'''
선택 정렬, O(N^2)
처리되지 않은 데이터 중 가장 작은 데이터를 선택해 바꿈  
'''
def sort_select(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        # 위치 swap
        array[i], array[min_index] = array[min_index], array[i]

    print(array)

'''
삽입 정렬, O(N^2)
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입, 선택 정렬보다 더 효율적
특징 : 거의 정렬되어 있는 경우 매우 빠르게 동작함
'''
def sort_insert(array):
    # 2번째위치부터 바로 왼쪽과 비교하는걸 반복
    for i in range(1, len(array)): # 두번째 위치부터 시작
        for j in range(i, 0, -1): # i부터 시작해서 1까지 -1
            if array[j] < array[j-1]: # 왼쪽과 비교해서 위치바꿈
                array[j], array[j-1] = array[j-1], array[j]
            else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
    print(array)

'''
퀵정렬, pivot 어떻게 설정하느냐에 따라 평균적으로 O(NlongN), 최악의 경우(이미 정렬된 경우)엔 O(N^2)
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은데이터의 위치를 바꿈
초기 pivot은 가장 왼쪽, > 방향으로 기준보다 큰것 선택, < 방향으로 기준보다 작은것 선택하여 위치를 서로 바꿈
엇갈리면 pivot 위치를 바꾸고 좌우를 분할 한뒤 재귀적으로 반복   
'''
def sort_quick(array, start, end):
    if start >= end:
        return # 원소가 1개인 경우 종료
    pivot = start # 첫번째 원소를 기준으로 설정

    left = start + 1 # 피벗기준 가장 왼쪽
    right = end # 피벗기준 가장 오른쪽

    while(left<=right): #엇 갈릴 떄 까지 반복
        # 왼쪽 부분: 피벗보다 큰 데이터 찾을떄까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 오른쪽 부분: 피벗보다 작은 데이터 찾을떄까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -=1
        # 교차되면 피벗값 변경(작은 데이터와 피벗값을 변경, right 값)
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 교차인 경우가 아니면 작은 데이터와 큰데이터를 교체
            array[left], array[right] = array[right], array[left]
        # 분할해서 재귀실행
        sort_quick(array, start, right-1)
        sort_quick(array, right +1, end)
    # print(array)

'''
간결한 버전의 quick sort
'''
def sort_quick2(array):
    # 리스트 하나의 원소를 담고있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 첫번째 원소를 피벗으로 설정
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]
    return sort_quick2(left_side) +[pivot] +sort_quick2(right_side)

'''
계수 정렬, O(N+k)
특정 조건 만족시 매우 빠름, 카운트 테이블을 만들어야 하므로 공간복잡도는 높은편
0과 999999, 단 2개만 존재하는 경우와 같이 매우 비효율적인 경우있음 
But 동일한 값을 가지는 데이터가 여러개 등장할때 효과적!(성적과 같이) 

가장 작은 데이터부터~ 가장 큰 데이터까지 모두 담길수 있는 리스트 생성 
=> 데이터값과 동일한 인덱스를 1 증가시켜서 Count table을 갱신시킴 
=> 그 인덱스의 개수(count)만큼 출력시킴 
'''
def sort_count(array):
    # 카운트 테이블 생성
    count = [0] * (max(array)+1)
    for i in range(len(array)):
        count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가
    for i in range(len(count)): # 카운트 테이블에 기록된 정렬 정보 출력
        for j in range(count[i]):
            print(i,end=' ')

# 연습문제, 두 배열의 원소교체
'''
N개의 자연수 원소를 가진 두 배열 A, B
최대 K 번의 바꿔치기 연산을 하여 A 배열의 합이 최대가 되도록
'''
def exercise_quicksort(array):
    if len(array) ==1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot ]

    return exercise_quicksort(left_side) + [pivot] + exercise_quicksort(right_side)


def exercise_sorting():
    N, K = map(int, input().split())
    print(N,K)
    array_A = list(map(int, input().split()))
    print(array_A)
    array_B = list(map(int, input().split()))
    print(array_B)

    # A의 최소값과 B의 최대값 교환 => A는 오름차순, B는 내림차순 정렬
    array_A.sort()
    array_B.sort(reverse=True)
    for i in range(K):
        if array_A[i] < array_B[i]:
            array_A[i], array_B[i] = array_B[i], array_A[i]
        else:
            break
    print(sum(array_A))
    sorted_A = exercise_quicksort(array_A)
    print(sorted_A)
    sorted_B = exercise_quicksort(array_B).reverse()
    print(sorted_B)

    for i in range(K):
        sorted_A[i], sorted_B[i] = sorted_B[i], sorted_A[i]
    print(sorted_A)

# 실전문제 2. 위에서 아래로 , 큰수부터 작은 수로 정렬하는 프로그램
def exercise_2():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(nums)
    nums.sort(reverse=True)
    print(nums)
    for i in nums:
        print(i, end=' ')

# 실전문제 3. 성적이 낮은 순서로 학생 출력하기
def exercise_3():
    n = int(input())
    names_scores = []

    for _ in range(n):
        name, score = input().split()
        names_scores.append((name, int(score)))

    print(names_scores)
    names_scores = sorted(names_scores, key=lambda names_scores : names_scores[1])
    print(names_scores)
    for name, _ in names_scores:
        print(name, end = ' ')
        

if __name__ == '__main__':
    # array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    # print(array)

    # sort_select(array)

    # sort_insert(array)

    # sort_quick(array, 0, len(array)-1)
    # print(array)

    # print(sort_quick2(array))

    # sort_count(array)

    # exercise_sorting()

    # exercise_2()
    exercise_3()
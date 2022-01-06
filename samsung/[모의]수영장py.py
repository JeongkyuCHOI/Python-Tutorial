import sys

sys.stdin = open("sample_input (수영장).txt", "r")


def dfs(month, cost):
    global is_min
    # 종료조건
    if month >= 12:
        if is_min > cost:
            is_min = cost
        return

    if plan[month] * fare[0] < fare[1]:
        # 1일 이용권으로 하는 경우가 한달보다 쌀때
        dfs(month +1, cost +plan[month]*fare[0])
    else:
        # 한달이용권이 더 쌀 때
        dfs(month+1, cost + fare[1])

    if plan[month] != 0:
        # 해당 월의 값이 0이면 3달 이용권 시작할 필요 없음
        dfs(month+3, cost + fare[2])



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    fare = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    is_min = fare[3] # 1년 이용권을 넣어서 확인하기
    dfs(0, 0)
    print("{} {}".format(test_case, is_min))
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
# table[i][0] : day
# table[i][1] : profit
'''
depth 가 정해져있음, 즉 유한한 길이의 경우를 탐색하는 것이므로 DFS 쓰자 
'''

is_max = 0
def dfs(day, profit):

    # 종료 조건
    if day == n:
        global is_max
        is_max = max(is_max, profit)
        return

    # 탐색 조건
    # 해당 일자의 Ti를 고려할 때, 상담할 수 있으면
    if (day + table[day][0]) <= n :
        cost = table[day][1]
        dfs(day+table[day][0], profit+cost)
    
    # 다른 경우도 확인 
    dfs(day+1, profit)

dfs(0, 0)
print(is_max)

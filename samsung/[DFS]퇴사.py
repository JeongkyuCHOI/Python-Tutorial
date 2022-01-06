n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

candidates = 0
def dfs(day, graph, profit):
    global candidates
 
    # 종료 조건, day가 n이 될 경우
    if day == n: 
        candidates = max(profit, candidates)
        return 

    # day의 상담을 수행할 수 있는 경우
    next_day = day + graph[day][0]
    if next_day <= n:
        Pi = graph[day][1]
        dfs(next_day, graph, profit+Pi)
    
    # 다음 일자 탐색
    dfs(day+1, graph, profit)

dfs(0, table, 0)
print(candidates)
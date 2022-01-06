from copy import deepcopy

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def rotate(graph): 
    n = len(graph) # 세로 행 y
    m = len(graph[0]) # 가로 열 x
    # new_lst = [[0]*n for _ in range(m)]
    new_lst = deepcopy(graph)
 
    for i in range(n):
        for j in range(m):
            # 시계방향 90도
            new_lst[j][n-i-1] = graph[i][j]
    return new_lst

def convert(N, graph):
    new_lst = [i for i in graph if i!=0] # 0을 제외한 부분 list에 저장
    for i in range(1, len(new_lst)):
        # 같은 숫자를 만난 경우
        if new_lst[i-1] == new_lst[i]:
            new_lst[i-1] *= 2
            new_lst[i] = 0
    new_lst = [i for i in new_lst if i != 0] #이동 후 0이 아닌부분 list에 저장 
    return new_lst + [0]*(N - len(new_lst)) # 합쳐진 원소 수만큼 오른쪽에 0추가

def dfs(N, graph, cnt):
    result = max([max(i) for i in graph]) # 최대값
    if cnt == 0:
        return result
    
    for _ in range(4): # 4방향이동
        C = [convert(N, i) for i in graph] # 그래프를 한줄씩 이동한 뒤 합침
        result = max(result, dfs(N, C, cnt -1))
        graph = rotate(graph) # 회전
    return result
    
answer = dfs(N, graph, 5)
print(answer)
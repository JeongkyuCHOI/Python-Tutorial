# Graph
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [4, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]
# Visited
visited = [False] * 9

# DFS (STACK, 재귀)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# BFS (QUEUE)
from collections import deque
def bfs(graph, start, visited):
    visited[start] = True

    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]: # 방문한 적이 없으면
                queue.append(i)
                visited[i] = True

dfs(graph, 1, visited)
visited = [False] * 9
bfs(graph, 1, visited)
# 1 2 7 6 8 3 4 5 1 2 3 8 7 4 5 6 
## 5-7 인접 리스트 방식 예제
'''
    0
 (7) (5)
1       2
'''
graph = [[] for _ in range(3)]

graph[0].append((1,7)) # 노드 0 노드 1 연결 거리 7
graph[1].append((0,7)) # 노드 1 노드 0 연결 거리 7

graph[0].append((2,5)) # 노드 0 <> 2, 연결거리 5
graph[2].append((0,5)) # 노드 2 <> 0, 연결 거리 5

print(graph)

## 인접 행렬 방식 예제
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [6, INF, 0]
]

print(graph)

'''
인접 행렬 방식은 메모리 낭비가 많으나 정보를 얻는 속도가 빠르다
인접 리스트 방식은 메모리낭비가 적으나 정보를 얻는 속도가 느리다
'''

## DFS : Depth-first search
'''
DFS는 깊이 우선탐색, 스택을 이용, 간단 O(N)
1) 탐색 시작 노드를 스택에 삽입하고 방문처리
2) 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
                     방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
3) 1-2번 반복
'''
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end= ' ')

    # 현재 노드와 인접한 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 방문한 노드가 아니면
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9
dfs(graph, 1, visited)


## BFS : Breadth-first search
'''
BFS는 너비 우선탐색, 큐을 이용, 간단 O(N), DFS보다 조금더 빠름
1) 탐색 시작 노드를 큐에 삽입하고 방문처리
2) 큐에서 노드를 꺼내 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
3) 1-2번 반복
'''
from collections import deque
def bfs(graph, start, visited):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] =True

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 노드와 연결된 아직 방문하지 않은 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
bfs(graph, 1, visited)

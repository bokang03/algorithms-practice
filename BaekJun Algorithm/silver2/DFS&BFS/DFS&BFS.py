from collections import deque

def dfs(graph, v, visited_dfs) :
    visited_dfs[v] = True
    print(v, end = " ")
    for i in range(1, len(graph)):
        if graph[v][i] == 1 and visited_dfs[i] == False :
            dfs(graph, i, visited_dfs)

def bfs(graph, v, visited_bfs):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:  # 큐가 빌 때까지 반복
        current = queue.popleft()  # 현재 노드 꺼내기
        print(current, end=' ')

        for i in range(1, len(graph)):
            if graph[current][i] == 1 and visited_bfs[i] == False:
                queue.append(i)
                visited_bfs[i] = True  # 큐에 넣을 때 방문 처리

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[0] * (n+1) for i in range(n+1)]

    visited_dfs = [False] * (n+1)
    visited_bfs = visited_dfs.copy()

    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    dfs(graph, v, visited_dfs)
    print()
    bfs(graph, v, visited_bfs)
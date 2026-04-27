from collections import deque


def bfs(graph, x, visited):
    visited[x] = True
    queue = deque([x])

    while queue:
        n = queue.popleft()
        print(n, end=" ")

        for i in graph[n]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

if __name__ == "__main__":
    graph = [
        [],
        [2, 3],
        [1, 4],
        [1, 5],
        [2],
        [3]
    ]
    visited = [False] * 6
    bfs(graph, 1, visited)
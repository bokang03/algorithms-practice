from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    count_num = [0 if i < 2 else 20001 for i in range(n + 1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    visited = [False] * (n + 1)
    visited[1] = True

    def bfs(num):
        ct = 0
        queue = deque([(num, ct)])

        while queue:
            number, ct1 = queue.popleft()
            for i in graph[number]:
                if visited[i] == False:
                    visited[i] = True
                    count_num[i] = ct1 + 1
                    queue.append((i, ct1 + 1))

    bfs(1)

    return count_num.count(max(count_num))
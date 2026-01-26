import sys
from collections import deque

def bfs(i):
    visited[i] = True
    queue = deque([i])

    while queue :
        k = queue.popleft()

        for j in arr[k] :
            if visited[j] == False :
                visited[j] = True
                queue.append(j)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)

    visited = [True] + [False]*n

    ct = 0
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            ct += 1

    print(ct)
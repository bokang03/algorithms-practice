from collections import deque
import sys

def bfs(k) :
    queue = deque([k])

    while queue :
        num = queue.popleft()

        for i in arr[num] :
            if visited[i] == True :
                continue
            visited[i] = True
            queue.append(i)
            result[i] = num

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    visited = [False] * (n+1)
    arr = [[] for _ in range(n+1)]
    result = [[]for _ in range(n+1)]
    for i in range(n-1) :
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    bfs(1)

    for i in range(2, n+1) :
        print(result[i])
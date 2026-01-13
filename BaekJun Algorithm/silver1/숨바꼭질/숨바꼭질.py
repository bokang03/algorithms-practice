from collections import deque
import sys

def bfs(n) :
    visited = {}
    queue = deque()
    queue.append(n)
    visited[n] = 0

    while True:
        num = queue.popleft()
        if num == k :
            return visited[k]
        for i in (num-1, num + 1, num * 2) :
            if 0 <= i <= 100000 and i not in visited :
                visited[i] = visited[num] + 1
                queue.append(i)


if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())

    print(bfs(n))




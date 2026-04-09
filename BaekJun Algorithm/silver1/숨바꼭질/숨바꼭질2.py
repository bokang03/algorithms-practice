from collections import deque
import sys

def bfs(num) :
    arr = []
    arr.extend([num - 1, num + 1, num * 2])
    queue = deque()

    for i in range(len(arr)) :
        queue.append([1, arr[i]])
        visited.append(arr[i])

    while queue :
        count, number = queue.popleft()
        if number == k :
            return count
        for i in [number - 1, number + 1, number * 2]:
            if 0 <= i <= 100000 and i not in visited:
                visited.append(i)
                queue.append((count + 1, i))

    return 0


if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    visited = []
    if n == k :
        print(0)
    else : print(bfs(n))

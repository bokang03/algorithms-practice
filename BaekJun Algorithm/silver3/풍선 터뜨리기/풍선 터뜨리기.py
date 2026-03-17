from collections import deque
import sys

if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))

    queue = deque()
    for i in range(N):
        queue.append((i + 1, arr[i]))

    answer = []

    while queue:
        num, move = queue.popleft()
        answer.append(num)

        if not queue:
            break

        if move > 0:
            for _ in range(move - 1):
                x = queue.popleft()
                queue.append(x)
        else:
            for _ in range(-move):
                x = queue.pop()
                queue.appendleft(x)

    for i in answer :
        print(i, end=" ")
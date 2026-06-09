from collections import deque

def solution(k, m, score):
    answer = 0
    arr = []

    queue = deque(sorted(score, reverse=True))

    while queue:
        apple = queue.popleft()
        arr.append(apple)

        if len(arr) == m:
            answer += m * arr[-1]
            arr = []

    return answer
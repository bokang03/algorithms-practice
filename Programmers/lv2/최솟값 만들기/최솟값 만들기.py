from collections import deque


def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    queue1 = deque(A)
    queue2 = deque(B)

    while queue1:
        a = queue1.popleft()
        b = queue2.popleft()

        answer += a * b

    return answer
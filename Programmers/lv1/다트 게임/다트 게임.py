from collections import deque


def solution(dartResult):
    answer = []
    queue = deque(dartResult)

    while queue:
        n = queue.popleft()

        if n.isdigit():
            if queue and queue[0].isdigit():
                next_n = queue.popleft()
                n += next_n
            answer.append(int(n))

        elif n == "*":
            if len(answer) == 1:
                answer[-1] *= 2
            else:
                answer[-1] *= 2
                answer[-2] *= 2

        else:
            num = answer.pop()
            if n == "D":
                answer.append(num ** 2)
            elif n == "T":
                answer.append(num ** 3)
            elif n == "S":
                answer.append(num ** 1)
            elif n == "#":
                answer.append(-num)

    return sum(answer)
from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    total = sum1 + sum2
    mid = total // 2
    limit = len(queue1) * 3

    if mid < max(queue1) or mid < max(queue2) or total % 2 == 1:
        return -1

    else:
        answer = 0

        while sum1 != sum2:
            answer += 1
            limit -= 1

            if sum1 > sum2:
                n = queue1.popleft()
                sum1 -= n
                queue2.append(n)
                sum2 += n
            else:
                n = queue2.popleft()
                sum2 -= n
                queue1.append(n)
                sum1 += n

            if limit < 0:
                return -1

        return answer
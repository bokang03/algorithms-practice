from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    dp = [-1] * (y + 1)
    dp[x] = 0
    queue = deque([x])

    while queue:
        curr = queue.popleft()

        for next_num in [curr + n, curr * 2, curr * 3]:
            if next_num <= y and dp[next_num] == -1:
                dp[next_num] = dp[curr] + 1
                if next_num == y:
                    return dp[next_num]
                queue.append(next_num)

    return dp[y]
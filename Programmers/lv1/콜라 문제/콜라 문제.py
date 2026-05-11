def solution(a, b, n):
    dp = [0] * (n + 1)

    for empty in range(a, n + 1):
        exchanged = (empty // a) * b
        remaining = (empty % a) + exchanged

        dp[empty] = exchanged + dp[remaining]

    return dp[n]
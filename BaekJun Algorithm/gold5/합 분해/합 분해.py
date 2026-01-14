if __name__ == '__main__' :
    n, k = map(int, input().split())

    dp = [[0] * (k+1) for i in range(n+1)]

    dp[0][0] = 1

    for i in range(n+1) :
        for k in range(1, k+1) :
            dp[i][k] = dp[i-1][k] + dp[i][k-1]

    print(dp[n][k] % 1000000000)
if __name__ == '__main__' :
    n = int(input())

    dp = [[0] * 10 for i in range(n+1)]

    for i in range(1, 10) :
        dp[1][i] = 1

    for i in range(2, n+1) :
        for k in range(10) :
            if k == 0 :
                dp[i][k] = dp[i-1][1] # 앞자리 0 은 없어야 하므로
            elif k == 9 :
                dp[i][k] = dp[i-1][8]
            else :
                dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]

    print(sum(dp[n]) % 1000000000)

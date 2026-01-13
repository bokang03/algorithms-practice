
if __name__ == '__main__' :
    n = int(input())
    dp = [[0]* 10 for  i in range(n+1)]

    for i in range(10) :
        dp[1][i] = 1 # 0 1 2 3 4 5 6 7 8 9

    for i in range(2, n+1):
        for k in range(10):
            if k == 0 :
                dp[i][k] = 1
            else :
                dp[i][k] = dp[i-1][k] + dp[i][k-1]


    print(sum(dp[n])%10007)

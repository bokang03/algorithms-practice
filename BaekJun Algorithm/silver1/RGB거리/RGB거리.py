
if __name__ == '__main__' :
    n = int(input())
    homes = []
    dp = [[0, 0, 0] for _ in range(n)]

    for _ in range(n) :
        colors = list(map(int,input().split()))
        homes.append(colors)

    dp[0][0] = homes[0][0]
    dp[0][1] = homes[0][1]
    dp[0][2] = homes[0][2]

    for i in range(1, n) :
        #  i 번째 빨
        dp[i][0] = homes[i][0] + min(dp[i-1][1], dp[i-1][2])
        #  i 번째 파
        dp[i][1] = homes[i][1] + min(dp[i-1][0], dp[i-1][2])
        #  i 번째 초
        dp[i][2] = homes[i][2] + min(dp[i-1][0], dp[i-1][1])


    print(min(dp[n-1]))
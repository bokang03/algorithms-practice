if __name__ == "__main__":
    result = []
    for _ in range(int(input())):
        k = int(input())
        n = int(input())
        dp = [[0] * (n+1) for _ in range(k+1)]
        dp[0] = [i for i in range(n+1)]

        for i in range(1, k+1) : # 층
            for j in range(1, n+1) :
                dp[i][j] = sum(dp[i-1][:j+1])

        result.append(dp[k][n])


    for i in result :
        print(i)

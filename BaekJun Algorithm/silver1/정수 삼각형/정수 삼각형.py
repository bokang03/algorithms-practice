if __name__ == "__main__" :
    n = int(input())
    arr = []
    for i in range(n) :
        stage = list(map(int, input().split()))
        arr.append(stage)


    if n == 1 :
        print(arr[0][0])
    else :
        dp = [[0] * i for i in range(1, n + 1)]

        for i in range(n) :
            for k in range(len(arr[i])) :
                if k == 0 :
                    dp[i][k] = arr[i][k] + dp[i-1][k]
                elif k == len(arr[i]) - 1:
                    dp[i][k] = arr[i][k] + dp[i-1][k-1]
                else :
                    dp[i][k] = arr[i][k] + max(dp[i-1][k-1], dp[i-1][k])

        print(max(dp[n-1]))

if __name__ == '__main__':
    n = int(input())
    arr = [input().split() for _ in range(n)]

    dp = [[0]* n for _ in range(n)]
    dp[0][0] = 1 # 시작은 0, 0

    for i in range(n) :
        for k in range(n):
            w = int(arr[i][k]) # 현재 위치

            if w == 0 or dp[i][k] == 0 :
                continue

            if i+w < n :
                dp[i+w][k] += dp[i][k]

            if k+w < n :
                dp[i][k+w] += dp[i][k]


    print(dp[n-1][n-1])
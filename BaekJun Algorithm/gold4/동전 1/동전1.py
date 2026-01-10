
if __name__ == '__main__':
    n, k = map(int, input().split())
    num = [int(input()) for _ in range(n)]
    dp = [0] * (k+1)
    dp[0] = 1

    for i in num :
        for m in range(i, k+1):
            dp[m] += dp[m-i]

    print(dp[k])

if __name__ == '__main__':
    n, k = map(int,input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    dp = [10001] * (k+1)
    dp[0] = 0

    for coin in arr :
        for j in range(coin, k+1) :
            dp[j] = min(dp[j], dp[j - coin] + 1)


    if dp[k] == 10001 :
        print(-1)
    else : print(dp[k])

    print(dp)
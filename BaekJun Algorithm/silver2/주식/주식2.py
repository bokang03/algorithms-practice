
if __name__ == '__main__':
    n = int(input())
    plans = []

    for i in range(n) :
        p = list(map(int, input().split()))
        plans.append(p)


    dp = [0] * (n+1)

    if plans[n-1][0] == 1 :
        dp[n-1] = plans[n-1][1]
    else :
        dp[n-1] = 0

    for i in range(n-2, -1, -1) :
        if n < i + plans[i][0] :
            dp[i] = dp[i+1]
        else :
            dp[i] = max(plans[i][1] + dp[i+ plans[i][0]], dp[i+1])


    print(dp[0])

if __name__ == '__main__':
    n = int(input())
    dp = [0] * (n+1)
    t = []
    p = []

    for _ in range(n) :
        t1, p1 = map(int,input().split())
        t.append(t1)
        p.append(p1)

    for i in range(n-1, -1, -1):
        print('i= ',  i)
        if t[i] + i > n :
            dp[i] = dp[i+1]

        else :
            dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])
    print(dp[0])
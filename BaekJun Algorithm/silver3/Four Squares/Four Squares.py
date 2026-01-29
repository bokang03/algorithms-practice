import sys
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    dp = [0] * (n + 1)

    num = 1
    while num ** 2 <= n:
        dp[num ** 2] = 1
        num += 1

    for i in range(1, n + 1):
        if dp[i] == 0:
            k = 1
            while k ** 2 <= i:
                if dp[i] == 0:
                    dp[i] = dp[k ** 2] + dp[i - k ** 2]
                else:
                    dp[i] = min(dp[i], dp[k ** 2] + dp[i - k ** 2])
                k += 1
        else : continue

    print(dp[n])

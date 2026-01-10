
if __name__ == "__main__" :
    dp = [1] * 10001
    result = []

    for _ in range(int(input())) :
        n = int(input())
        result.append(n)

    def dynamic() :
        for i in range(2, 10001) :
            dp[i] += dp[i-2]

        for i in range(3, 10001):
            dp[i] += dp[i-3]

    dynamic()

    for i in result:
        print(dp[i])
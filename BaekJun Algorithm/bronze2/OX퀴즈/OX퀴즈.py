if __name__ == '__main__' :

    n = int(input())
    dp = [0] * 81
    result = []

    for i in range(1, 81) :
        dp[i] = dp[i-1] + 1

    for i in range(n) :
        bingo = input()
        ct = 1
        total = 0
        for k in bingo :
            if k == "O" :
                total += dp[ct]
                ct += 1
            else :
                ct = 1
        result.append(total)

    for i in result  :
        print(i)
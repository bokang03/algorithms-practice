
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))

    dp = [0] *n
    dp[0] = arr[0]
    total = arr[0]

    for num in range(1, n) :
        dp[num] = max(dp[num-1] + arr[num], arr[num])


    print(max(dp))
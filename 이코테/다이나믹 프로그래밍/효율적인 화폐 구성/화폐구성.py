if __name__ == '__main__':

    n, m = map(int, input().split())
    coin = []
    d = [10001] * (m+1)
    d[0] = 0

    for i in range(n) :
        coin.append(int(input()))

    for i in range(n):
        for k in range(coin[i], m+1):
            if d[k - coin[i]] != 10001:
                d[k] = min(d[k], d[k - coin[i]] + 1)


    if d[m] == 10001:
        print(-1)
    else :
        print(d[m])
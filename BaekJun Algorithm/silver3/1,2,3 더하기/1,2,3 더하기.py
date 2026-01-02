def fibo(n):
    for i in range(1, n+1):
        if i == 1:
            d[1] = 1
        elif i == 2:
            d[2] = 2
        elif i == 3:
            d[3] = 4
        else:
            d[i] = d[i - 3] + d[i - 2] + d[i - 1]
    return d[n]


if __name__ == '__main__':
    n = int(input())
    d = [0] * 12
    result = 0
    arr = []

    for i in range(n):
        arr.append(int(input()))

    for i in arr :
        print(fibo(i))
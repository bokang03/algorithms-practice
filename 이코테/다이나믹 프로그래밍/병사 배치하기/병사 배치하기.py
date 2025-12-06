if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    d = [1] * n

    for i in range(1, n) :
        for k in range(0, i):
            if arr[k] < arr[i] :
                d[i] = max(d[i], d[k]+1)

    print(n-max(d))
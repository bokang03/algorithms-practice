if __name__ == '__main__' :
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse= True)

    for i in range(M) :
        a[i], b[i] = b[i], a[i]

    print(sum(a))

if __name__ == '__main__' :
    num = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ct = 0
    result = 0

    for i in arr :
        ct += 1
        if ct >= i :
            result += 1
            ct = 0

    print(result)
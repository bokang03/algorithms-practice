if __name__ == '__main__':
    n, k = map(int, input().split())
    ct = 0
    while (n > 1) :
        if n % k == 0 :
            n //= k
        else : n -= 1
        ct += 1

    print(ct)
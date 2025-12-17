if __name__ == '__main__':
    N = int(input())
    a = 666
    count = 0

    while True :
        if "666" in str(a) :
            count += 1
        if count == N :
            print(a)
            break
        a += 1
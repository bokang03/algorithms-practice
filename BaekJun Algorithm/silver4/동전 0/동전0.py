
if __name__ == '__main__':
    n, k = map(int, input().split())
    coin = []
    count = 0

    for i in range(n):
        coin.append(int(input()))

    coin.sort(reverse= True)


    for i in coin :
        if i > k :
            continue

        count += k // i
        k = k%i
        if k == 0 :
            break

    print(count)

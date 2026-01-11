if __name__ == '__main__' :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(m) :
        arr.sort()
        card1 = arr[0]
        card2 = arr[1]

        card = card1 + card2

        x = arr.index(card1)
        y = arr.index(card2)

        arr[0] = card
        arr[1] = card

    print(sum(arr))

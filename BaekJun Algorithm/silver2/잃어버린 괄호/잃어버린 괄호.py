if __name__ == '__main__':
    n = input().split('-')

    arr = []

    for i in n :
        sum = 0
        plus_num = i.split("+")
        for k in plus_num :
            sum += int(k)
        arr.append(sum)


    st = arr[0]

    for i in range(1, len(arr)):
        st -= arr[i]

    print(st)
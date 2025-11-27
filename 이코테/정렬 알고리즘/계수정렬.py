if __name__ == '__main__' :
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

    ct = [0] * (max(arr) + 1)

    for i in range(len(arr)) :
        ct[arr[i]] += 1

    for i in range(len(ct)) :
        for k in range(ct[i]) :
            print(i, end=' ')
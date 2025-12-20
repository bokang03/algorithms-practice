if __name__ == '__main__':
    n = int(input())
    ct = 0

    for i in range(n):
        m = input()
        arr = []
        result = True
        # 그룹 단언 판별
        for i in m:
            if i in arr:
                if i != arr[-1]:
                    result = False
                    break
                else:
                    continue
            arr.append(i)
        if result == True:
            ct += 1

    print(ct)
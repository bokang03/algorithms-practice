
if __name__ == '__main__':
    n = int(input())

    arr = []
    result = []
    head = 0
    h = False
    for i in range(n) :
        cokie = list(input())
        if "*" in cokie and h == False :
            head = [i, cokie.index("*")]
            h = True
        arr.append(cokie)

    heart = [head[0] + 1, head[1]]
    result_head = [head[0]+2, head[1]+1] # 출력

    # 왼팔
    ct = 0
    for i in range(heart[1]):
        if arr[heart[0]][i] == "*" :
            ct += 1

    result.append(ct)

    ct = 0

    for i in range(heart[1]+1, n) :
        if arr[heart[0]][i] == "*" :
            ct += 1

    result.append(ct)

    ct = 0
    end = 0

    # 허리
    for i in range(heart[0]+1, n) :
        if arr[i][heart[1]] == "_" :
            end = i-1
            break
        ct += 1

    result.append(ct)
    ct= 0
    # 왼쪽 다리
    for i in range(end+1, n) :
        if arr[i][heart[1] - 1] ==  "_" :
            break
        ct += 1

    result.append(ct)

    ct = 0

    for i in range(end+1, n) :
        if arr[i][heart[1]+1] == "_" :
            break
        ct += 1

    result.append(ct)

    print(' '.join(map(str, result_head)))
    print(' '.join(map(str, result)))
import sys

def dfs(y, x, n) :
    color = arr[y][x]
    result = True

    for i in range(y, y+n) :
        if result == False :
            break
        for k in range(x, x+n) :
            if arr[i][k] != color :
                result = False

    if not result:
        num = n//2
        dfs(y, x, num)
        dfs(y+num, x, num)
        dfs(y, x+num, num)
        dfs(y + num, x + num, num)
    else :
        colors[color] += 1
        return


if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    arr = []

    # 인덱스 0 = 하양 , 1은 파랑
    colors = [0, 0]

    for i in range(n) :
        arr.append(list(map(int, input().split())))

    dfs (0,0,n)

    print(colors[0])
    print(colors[1])
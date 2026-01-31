
if __name__ == "__main__" :
    n = int(input())
    result = [[0]*100 for i in range(100)]

    for _ in range(n):
        x, y = map(int, input().split())

        for i in range(x,x+10) :
            for k in range(y, y+10):
                result[i][k] = 1

    ct = 0

    for i in range(100) :
        ct += result[i].count(1)

    print(ct)


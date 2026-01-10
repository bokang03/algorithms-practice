import sys
if __name__ == '__main__':
    input = sys.stdin.readline
    arr = []

    for _ in range(int(input())):
        arr.append(int(input()))

    if len(arr) <= 1 :
        ct = 0
    else :
        me = arr[0]
        cmp = arr[1:]
        ct = 0

        while me <= max(cmp) :
            x = cmp.index(max(cmp))
            cmp[x] -= 1
            me += 1
            ct += 1

    print(ct)
import sys

if __name__ == '__main__' :
    input = sys.stdin.readline

    k, n = map(int,input().split())
    line = []

    for i in range(k):
        line.append(int(input()))

    st, end = 1, max(line)
    ans = 0
    while st <= end :
        mid = (st + end)//2
        total = 0
        for i in line :
            if i >= mid :
                total += i//mid

        if total >= n :
            ans = mid
            st = mid + 1
        else :
            end = mid - 1

    print(ans)
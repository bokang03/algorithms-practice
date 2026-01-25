import sys
if __name__ == '__main__' :
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = [0]

    total = 0

    for i in range(n) :
        total += arr[i]
        result.append(total)

    for _ in range(m) :
        i, j = map(int, input().split())
        ans = result[j] - result[i-1]
        print(ans)
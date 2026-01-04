def dfs():
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in range(n) :
        result.append(arr[i])
        dfs()
        result.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = []

    dfs()
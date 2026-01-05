def dfs(v):
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in range(v, len(arr)):
        result.append(arr[i])
        dfs(i)
        result.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    result = []

    dfs(0)
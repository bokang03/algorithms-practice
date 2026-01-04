def dfs(start):
    if len(result) == m :
        print(' '.join(map(str, result)))
        return

    for i in range(start, n):
        result.append(arr[i])
        dfs(i)
        result.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result =[]

    dfs(0)
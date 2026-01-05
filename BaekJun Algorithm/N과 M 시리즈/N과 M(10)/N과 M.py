def dfs(v):
    check = 0
    if len(result) == m :
        print(" ".join(map(str, result)))
        return

    for i in range(v, n) :
        if visited[i] == False and check != arr[i] :
            visited[i] = True
            result.append(arr[i])
            check = arr[i]
            dfs(i)
            result.pop()
            visited[i] = False

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = []
    visited = [False] * n

    dfs(0)

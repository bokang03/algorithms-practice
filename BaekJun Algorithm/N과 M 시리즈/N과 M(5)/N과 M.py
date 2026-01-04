def dfs():
    if len(result) == m :
        print(' '.join(map(str, result)))
    for i in range(n):
        if visited[i]:
            continue
        result.append(arr[i])
        visited[i] = True
        dfs()
        result.pop()
        visited[i] = False

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    visited = [False] * (n)
    result = []

    dfs()
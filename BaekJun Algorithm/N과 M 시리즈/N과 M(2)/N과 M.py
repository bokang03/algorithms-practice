def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n + 1):
        arr.append(i)
        dfs(i + 1)
        arr.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    dfs(1)

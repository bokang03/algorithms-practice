def dfs(x, y):

    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if visited[x][y] == True:
        return False

    if ice_frame[x][y] == 0:
        visited[x][y] = True

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


if __name__ == '__main__':
    N, M = map(int, input().split())
    ice_frame = []
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        ice_frame.append(list(map(int, list(input()))))

    result = 0

    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1

    print(result)
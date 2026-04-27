from collections import deque

def bfs(x, y, visited, land, answer) :
    p = set()
    if visited[y][x] == True or land[y][x] == 0:
        return 0
    ct = 1
    visited[y][x] = True
    queue = deque([(x,y)])

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue :
        x1, y1 = queue.popleft()
        p.add(x1)
        for i in range(4) :
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < len(land[0]) and 0 <= ny < len(land) :
                if visited[ny][nx] == False and land[ny][nx] == 1 :
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    p.add(nx)
                    ct += 1
    p = list(p)
    for l in p :
        answer[l] += ct
    return ct

def solution(land):
    n = len(land) # 세로
    m = len(land[0]) #가로
    answer = [0 for _ in range(m)]
    visited = [[False]*m for _ in range(n)]

    for i in range(m) :
        total = 0
        for k in range(n) :
            bfs(i, k, visited, land, answer)

    return max(answer)
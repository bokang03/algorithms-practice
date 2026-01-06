from collections import deque

def bfs(w, h):
    queue = deque([(w, h)])
    arr[w][h] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))

if __name__ == '__main__':
    result = []

    for _ in range(int(input())) :
        m, n, k = map(int,input().split())
        arr = [[0] * m for _ in range(n)]
        count = 0

        for j in range(k) :
            a, b = map(int, input().split())
            arr[b][a] = 1

        for z in range(n) :
            for q in range(m) :
                if arr[z][q] == 1 :
                    count += 1
                    bfs(z, q)
        result.append(count)

    for i in result :
        print(i)
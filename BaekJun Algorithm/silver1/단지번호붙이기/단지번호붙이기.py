from collections import deque

def bfs(x, y) :
    arr[x][y] = 0
    count = 1
    # 좌우위아래
    queue = deque([(x, y)])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue :
        a, b = queue.popleft()
        for i in range(4):
            x1 = a + dx[i]
            y1 = b + dy[i]
            if 0 <= x1 < n and 0 <= y1 < len(arr[0]) and arr[x1][y1] == 1:
                arr[x1][y1] = 0
                queue.append((x1, y1))
                count += 1
    result.append(count)

if __name__ == '__main__':
    n = int(input())
    arr = []
    result = []

    for i in range(n):
        city = list(map(int,input()))
        arr.append(city)

    for i in range(n):
        for k in range(len(arr[i])):
          if arr[i][k] == 1 :
            bfs(i, k)

    # 출력
    print(len(result))
    result.sort()
    for i in result:
        print(i)
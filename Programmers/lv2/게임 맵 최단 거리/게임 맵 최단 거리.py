from collections import deque

if __name__== '__main__':

    def solution(maps):
        # 상 하 좌 우
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def bfs(x, y, ct):
            maps[y][x] = 0
            queue = deque([(x, y, ct)])
            while queue:
                xx, yy, ctt = queue.popleft()
                if xx == len(maps[0])-1 and yy == len(maps)-1:
                    return ctt + 1
                for i in range(4):
                    nx = xx + dx[i]
                    ny = yy + dy[i]
                    if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] == 1:
                        maps[ny][nx] = 0
                        queue.append((nx, ny, ctt+1))
            return -1

        return bfs(0, 0, 0)

    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))
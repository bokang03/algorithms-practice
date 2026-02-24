def solution(board):
    n = len(board)
    bomb = []
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                bomb.append((y, x))

    # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우화
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    for y, x in bomb:
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[ny][nx] = 1

    ct = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                ct += 1
    return ct
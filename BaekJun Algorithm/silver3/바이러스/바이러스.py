def validator(d, start, visited) :
    visited[start] = True

    for i in range(1, len(d)):
        if d[start][i] == 1 and visited[i] == False :
            validator(d,i, visited)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    d = [[0]*(n+1) for i in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        d[a][b] = d[b][a] = 1

    validator(d, 1, visited)
    ct = sum(visited) - 1

    print(ct)
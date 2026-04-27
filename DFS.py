def dfs(graph, x, visited) :
    if visited[x] == True :
        return
    visited[x] = True
    print(x, end = " ")

    for i in graph[x] :
        dfs(graph, i, visited)



if __name__ == "__main__":
    graph = [
        [],
        [2, 3],
        [1, 4],
        [1, 5],
        [2],
        [3]
    ]
    visited = [False] * 6
    dfs(graph, 1, visited)
    # 1 2 4 3 5
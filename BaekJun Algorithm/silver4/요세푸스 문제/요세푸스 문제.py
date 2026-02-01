from collections import deque

if __name__ == "__main__" :
    n, k = map(int, input().split())
    queue = deque([i for i in range(1, n+1)])
    result = []
    ct = 0


    while queue :
        n = queue.popleft()
        ct += 1

        if ct == k :
            result.append(n)
            ct = 0
        else :
            queue.append(n)

    print(f"<{', '.join(map(str, result))}>")
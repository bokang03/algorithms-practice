import heapq

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []

    for i in range(len(arr)):
        arr[i] = -arr[i]

    heapq.heapify(arr)

    while arr:
        t = -heapq.heappop(arr)

        # 빈 콘센트 있음
        if len(result) < m:
            heapq.heappush(result, t)

        # 빈 콘센트 없음
        else:
            x = heapq.heappop(result)

            # 가장 빨리 끝나는 콘센트
            heapq.heappush(result, x + t)

    print(max(result))
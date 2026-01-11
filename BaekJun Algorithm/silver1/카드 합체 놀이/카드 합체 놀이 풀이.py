from heapq import heapify, heappop, heappush
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    heapify(arr)

    for _ in range(m):
        x = heappop(arr)+heappop(arr)
        heappush(arr, x); heappush(arr, x)

    print(sum(arr))
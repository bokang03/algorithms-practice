import heapq
import sys

if __name__ == "__main__" :
    input = sys.stdin.readline
    arr = []

    for _ in range(int(input())) :
        n = int(input())

        if n == 0 :
            if len(arr) == 0 :
                print(0)
            else :
                print(heapq.heappop(arr))
        else :
            heapq.heappush(arr, n)


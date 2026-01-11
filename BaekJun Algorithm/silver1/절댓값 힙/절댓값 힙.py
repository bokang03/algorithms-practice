import heapq as hq
import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    heap = []
    arr = dict()

    for i in range(n) :
        num = int(input())

        if num < 0 :
            if num not in arr :
                arr[num] = 1
            else :
                arr[num] += 1

            hq.heappush(heap, -num)

        elif num > 0 :
            hq.heappush(heap, num)

        else :
            if len(heap) == 0:
                print(0)
            else:
                number = hq.heappop(heap)
                if -number in arr and arr[-number] >= 1:
                    arr[-number] -= 1
                    print(-number)
                else : print(number)


import heapq

if __name__ == '__main__':
    n = int(input())
    arr = []
    ct = 0

    if n == 1 :
        print(0)
    else :
        for _ in range(n) :
            k = int(input())
            arr.append(-k)

        me = arr[0]
        cmp = arr[1:]
        heapq.heapify(cmp)

        while me >= min(cmp) :
            c = heapq.heappop(cmp)
            me -= 1
            heapq.heappush(cmp, c+1)
            ct += 1

        print(ct)


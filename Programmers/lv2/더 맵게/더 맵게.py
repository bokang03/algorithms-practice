import heapq

def solution(scoville, K):
    ct = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) <= 1:
            ct = -1
            break

        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville) * 2
        food = food1 + food2
        heapq.heappush(scoville, food)
        ct += 1

    return ct
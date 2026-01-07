from collections import deque

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    queue = deque(arr)

    result = []

    if len(arr)%2 == 1 :
        result.append(queue.pop())

    while queue :
        cal = queue.popleft() + queue.pop()
        result.append(cal)


    print(max(result))

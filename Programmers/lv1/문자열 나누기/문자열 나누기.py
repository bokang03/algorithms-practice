from collections import deque


def solution(s):
    answer = 0
    queue = deque(s)
    arr = []

    st = queue.popleft()
    arr.append(st)

    while queue:
        c = queue.popleft()

        if st == "":
            st = c
            arr.append(st)
            continue

        if c == st:
            arr.append(st)
        else:
            arr.append("0")

            if arr.count(st) == arr.count("0"):
                answer += 1
                st = ""
                arr = []

    if arr:
        answer += 1

    return answer
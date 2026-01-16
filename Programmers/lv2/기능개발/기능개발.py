from collections import deque

def solution(progresses, speeds):
    d = [0] * len(progresses)

    for i in range(len(progresses)):
        time = 100 - progresses[i]
        if time % speeds[i] != 0:
            d[i] = time // speeds[i] + 1
        else:
            d[i] = time // speeds[i]

    ct = 1
    d.append(101)
    queue = deque(d)
    answer = []

    st = queue.popleft()
    while queue:
        end = queue.popleft()
        if st >= end:
            ct += 1
        else:
            answer.append(ct)
            st = end
            ct = 1

    return answer
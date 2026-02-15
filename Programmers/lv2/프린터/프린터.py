def solution(priorities, location):
    ct = 0
    last = len(priorities)

    while priorities:
        n = priorities.pop(0)
        if len(priorities) == 0:
            break
        max_num = max(priorities)
        location -= 1

        if n < max_num:
            priorities.append(n)
            if location == -1:
                location = len(priorities) - 1
        else:
            ct += 1
            if location == -1:
                return ct
    return last
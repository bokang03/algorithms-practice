def solution(sizes):
    max_num = 0
    min_num = 10001
    for i in sizes:
        n = max(i)
        m = min(i)
        if n > max_num:
            max_num = n
        if m < min_num:
            min_num = m

    for size in sizes:
        if min(size) > min_num:
            min_num = min(size)

    answer = min_num * max_num
    return answer
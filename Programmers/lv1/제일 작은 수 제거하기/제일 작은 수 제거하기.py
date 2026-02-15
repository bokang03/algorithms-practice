def solution(arr):
    if len(arr) < 2:
        return [-1]

    min_num = min(arr)
    arr.remove(min_num)

    return arr
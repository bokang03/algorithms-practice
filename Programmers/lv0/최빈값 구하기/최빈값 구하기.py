def solution(array):
    answer = 0
    arr = set(array)
    result = [0] * 1001
    for i in arr:
        result[i] = array.count(i)

    max_num = max(result)

    if result.count(max(result)) > 1:
        answer = -1
    else:
        answer = result.index(max_num)

    return answer
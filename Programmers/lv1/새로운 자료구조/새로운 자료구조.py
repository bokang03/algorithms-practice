def solution(queries):
    answer = 0
    result = dict()

    for i in queries:
        if i in result:
            if result[i] == 1:
                result[i] = 0
            else:
                result[i] = 1
        else:
            result[i] = 1

    return sum(result.values())

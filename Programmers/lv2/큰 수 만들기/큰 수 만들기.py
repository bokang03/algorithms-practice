def solution(number, k):
    num = list(map(int, list(number)))
    result = []
    ct = 0

    for i in num:
        if not result:
            result.append(i)
            continue
        if k > 0:
            while result[-1] < i:
                result.pop()
                k -= 1
                if not result or k <= 0:
                    break

        result.append(i)

    result = result[:-k] if k > 0 else result
    return ''.join(map(str, result))

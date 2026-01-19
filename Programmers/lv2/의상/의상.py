def solution(clothes):
    a = dict()
    answer = 1
    for _, name in clothes:
        if name in a:
            a[name] += 1
        else:
            a[name] = 1

    for i, k in a.items():
        answer *= (k + 1)

    return answer - 1
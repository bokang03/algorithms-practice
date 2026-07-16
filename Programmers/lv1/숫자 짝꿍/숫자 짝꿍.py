def solution(X, Y):
    result = []
    num_dic = {}

    for i in range(10):
        a = min(X.count(str(i)), Y.count(str(i)))
        num_dic[i] = a

    for num, ct in num_dic.items():
        if ct == 0:
            continue

        result.append(str(num) * ct)

    if len(result) == 0:
        return "-1"

    result.sort(reverse=True)
    answer = "".join(result)

    if answer[0] == "0":
        return "0"

    return answer
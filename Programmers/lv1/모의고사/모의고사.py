def solution(answers):
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0] * 3

    for i in range(len(answers)):
        if answers[i] == st1[i % 5]:
            result[0] += 1

        if answers[i] == st2[i % 8]:
            result[1] += 1

        if answers[i] == st3[i % 10]:
            result[2] += 1

    max_num = max(result)
    answer = []

    for i in range(len(result)):
        if result[i] == max_num:
            answer.append(i + 1)

    return answer
def solution(x, m, myStr):
    answer = 0
    ct = 1

    for i in range(len(myStr) - 1, -1, -1):
        a = ord(myStr[i]) - ord('a') + 1
        answer += a * ct
        ct = (ct * x) % m

    return answer % m
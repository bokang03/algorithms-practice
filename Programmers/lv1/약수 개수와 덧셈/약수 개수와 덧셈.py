def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        ct = 0
        for n in range(1, num // 2 + 1):
            if num % n == 0:
                ct += 1
        if ct % 2 == 0:
            answer -= num
        else:
            answer += num

    return answer
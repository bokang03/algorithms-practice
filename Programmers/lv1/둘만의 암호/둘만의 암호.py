def solution(s, skip, index):
    answer = ''

    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]

    boundary = len(alphabet) - 1

    for i in s:
        num = (alphabet.index(i) + index) % len(alphabet)
        answer += alphabet[num]

    return answer
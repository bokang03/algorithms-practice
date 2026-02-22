def solution(s):
    answer = ""
    result = ""
    alphabat = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in s:
        if i.isdigit():
            result += str(i)
            continue

        answer += i
        if answer in alphabat:
            n = alphabat.index(answer)
            result += str(n)
            answer = ""

    return int(result)
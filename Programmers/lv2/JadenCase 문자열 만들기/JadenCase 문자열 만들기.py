def solution(s):
    answer = list(s.split(" "))

    for i in range(len(answer)):
        msg = answer[i]
        j = ""
        for k in range(len(msg)):
            if k == 0:
                if msg[k].isalpha() == True:
                    j += msg[k].upper()
                else:
                    j += msg[k]
            else:
                if msg[k].isalpha() == True:
                    j += msg[k].lower()
                else:
                    j += msg[k]
        answer[i] = j

    return ' '.join(map(str, answer))
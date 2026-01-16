def solution(s):
    answer = True

    if s[0] == ")" or s[-1] == "(":
        answer = False

    else:
        result = dict()
        result["("] = 1
        for i in range(1, len(s)):
            if s[i] == "(":
                result["("] += 1
            else:  # ) 이게 나온 경우
                if result["("] <= 0:
                    answer = False
                    break
                else:
                    result["("] -= 1

            if answer:
                if result["("] == 0:
                    answer = True
                else:
                    answer = False

    return answer
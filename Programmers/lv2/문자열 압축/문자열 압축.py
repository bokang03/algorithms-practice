def solution(s):
    answer = 1001

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        result = ""
        st = s[:i]
        ct = 1
        for k in range(i, len(s), i):
            if st == s[k: k + i]:
                ct += 1
            else:
                if ct > 1:
                    result += str(ct) + st
                else:
                    result += st
                ct = 1
                st = s[k: k + i]

        if ct > 1:
            result += str(ct) + st
        else:
            result += st
        answer = min(answer, len(result))

    return answer

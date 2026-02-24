def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                # a = 65, z= 90  a = 97, z = 123
                word = ord(i) + n
                if word > 122:
                    answer += chr(word - 26)
                else:
                    answer += chr(word)
            else: # 대문자
                new_ord = ord(i) + n
                if new_ord > 90:
                    answer += chr(new_ord - 26)
                else:
                    answer += chr(new_ord)
        else:
            answer += " "
    return answer
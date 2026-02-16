def solution(s):
    p_num = s.count("p") + s.count("P")
    s_num = s.count("y") + s.count("Y")

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    if p_num == s_num:
        return True
    else:
        return False
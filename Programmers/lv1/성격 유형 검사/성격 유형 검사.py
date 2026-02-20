def solution(survey, choices):
    # 1. 점수를 저장할 딕셔너리 초기화
    score_map = {}

    # 2. 설문 결과 계산
    for s, c in zip(survey, choices):
        if c < 4:
            # 비동의 계열 (앞 글자에 점수 부여)
            char = s[0]
            score_map[char] = score_map.get(char, 0) + (4 - c)
        elif c > 4:
            # 동의 계열 (뒷 글자에 점수 부여)
            char = s[1]
            score_map[char] = score_map.get(char, 0) + (c - 4)

    # 3. 성격 유형 판단 (StringBuilder 대신 문자열 조합)
    answer = ""
    answer += 'R' if score_map.get('R', 0) >= score_map.get('T', 0) else 'T'
    answer += 'C' if score_map.get('C', 0) >= score_map.get('F', 0) else 'F'
    answer += 'J' if score_map.get('J', 0) >= score_map.get('M', 0) else 'M'
    answer += 'A' if score_map.get('A', 0) >= score_map.get('N', 0) else 'N'

    return answer
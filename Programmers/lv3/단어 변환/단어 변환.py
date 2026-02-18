from collections import deque


def solution(begin, target, words):
    # 예제2 참고, words에 target이 없다면 return 0
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current_word, ct = queue.popleft()

        if current_word == target:
            return ct

        # words에서 정렬 위치 상관없이 교체 가능, 단 중복 word(X)
        for word in words:
            # 중복 제거
            if word not in visited:
                # 알파벳 하나만 변경 가능하니깐 1개 차이인 단어 선택
                ct2 = 0
                for i in range(len(word)):
                    if current_word[i] != word[i]:
                        ct2 += 1

                if ct2 == 1:
                    visited.add(word)
                    queue.append((word, ct + 1))

    return 0
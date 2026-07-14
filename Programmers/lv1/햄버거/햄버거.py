def solution(ingredient):
    answer = 0
    arr = []

    # 빵 1, 야채 2, 고기 3
    # 빵 - 야채 - 고기  - 빵
    buger = [1, 2, 3, 1]

    for i in ingredient:
        arr.append(i)
        if arr[-4:] == buger:
            answer += 1
            del arr[-4:]

    return answer
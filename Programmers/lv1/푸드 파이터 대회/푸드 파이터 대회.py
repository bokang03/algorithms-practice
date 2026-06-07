def solution(food):
    left_side = ""

    for i in range(1, len(food)):
        left_side += str(i) * (food[i] // 2)

    return left_side + "0" + left_side[::-1]
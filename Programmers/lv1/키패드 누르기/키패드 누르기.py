def solution(numbers, hand):
    answer = ''

    x = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    left = 10
    right = 11

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = num
        else:
            left_left = abs(x[num][0] - x[left][0]) + abs(x[num][1] - x[left][1])
            left_right = abs(x[num][0] - x[right][0]) + abs(x[num][1] - x[right][1])

            if left_left < left_right:
                left = num
                answer += "L"
            elif left_left > left_right:
                right = num
                answer += "R"
            else:
                if hand == "right":
                    answer += "R"
                    right = num
                else:
                    left = num
                    answer += "L"

    return answer
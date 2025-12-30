def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow%i == 0:
            width = int(yellow/i)
            height = i
            if (width * 2) + (height * 2) + 4 == brown :
                answer.append(width + 2)
                answer.append(height + 2)
                break
    answer.sort(reverse = True)
    return answer
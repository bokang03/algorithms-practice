def solution(numbers):
    answer = ''
    b = dict()

    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
        n = 4 - len(numbers[i])
        numbers[i] += (numbers[i][-1] * 3)
        b[numbers[i]] = 4 - n

    numbers.sort(key=lambda x: (int(x[0]), int(x[1]), int(x[2]), int(x[3])), reverse=True)

    for i in numbers:
        v = b[i]
        answer += i[:v]

    return answer

if __name__ == "__main__":
    numbers = [51, 15]
    print(solution(numbers))


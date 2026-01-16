def solution(array, commands):
    answer = []

    for command in commands:
        st = command[0] - 1
        end = command[1]
        cut_arr = array[st: end]
        cut_arr.sort()
        num = command[2] - 1
        answer.append(cut_arr[num])

    return answer
def solution(s):
    arr = s.split(" ")
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    arr.sort()
    answer = str(arr[0]) + " " + str(arr[-1])
    return answer

if __name__ == '__main__':
    s = input()
    print(solution(s))
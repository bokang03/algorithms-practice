import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    validate = list(map(int, input().split()))

    result = {}
    answer = []

    for i in range(len(arr)) :
        if arr[i] not in result :
            result[arr[i]] = 1
        else :
            result[arr[i]] += 1

    for i in validate :
        answer.append(result.get(i, 0))

    print(' '.join(map(str, answer)))

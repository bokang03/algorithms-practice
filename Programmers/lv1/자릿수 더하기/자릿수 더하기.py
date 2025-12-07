def solution(n):
    n = str(n)
    answer = 0

    for i in range(len(n)):
        answer += int(n[i])

    return answer

if __name__ == "__main__" :
    n = int(input())
    print(solution(n))
def solution(numbers):
    arr = list(numbers)
    visited = [False] * len(arr)
    result = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def backtracking(num):
        if num != "":
            result.add(int(num))

        for i in range(len(arr)):
            if visited[i]:
                continue
            visited[i] = True
            backtracking(num + arr[i])
            visited[i] = False

    backtracking("")

    answer = 0
    for x in result:
        if is_prime(x):
            answer += 1

    return answer
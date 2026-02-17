def solution(numbers, target):
    def backtracking(idx, current_sum):
        if idx == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0

        ct = 0
        ct += backtracking(idx + 1, current_sum + numbers[idx])
        ct += backtracking(idx + 1, current_sum - numbers[idx])

        return ct

    return backtracking(0, 0)
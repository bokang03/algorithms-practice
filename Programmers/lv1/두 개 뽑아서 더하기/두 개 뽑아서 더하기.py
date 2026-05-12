from itertools import permutations

def solution(numbers):
    answer = set()

    for i, k in permutations(numbers, 2):
        answer.add(i + k)

    return sorted(answer)
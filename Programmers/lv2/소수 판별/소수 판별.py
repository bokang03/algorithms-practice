from itertools import permutations

def solution(numbers):
    arr = []
    visited = []

    for i in range(1, len(numbers) + 1):
        n = permutations(numbers, i)
        arr.extend(n)

    ct = 0

    for i in list(set(arr)) :
        i = list(i)
        if i[0] == "0" :
            continue
        num = ''.join(map(str, i))
        num = int(num)
        if num < 2 :
            continue
        ct += 1
        for k in range(2, num):
            if num%k == 0 :
                visited.append(False)
                break
    return ct - len(visited)

if __name__ == "__main__":
    numbers = "011"
    print(solution(numbers))

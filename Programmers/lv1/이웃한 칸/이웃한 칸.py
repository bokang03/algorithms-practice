def solution(number, limit, power):
    arr = [1]

    for num in range(2, number + 1):
        count = 2

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if i * i == num:
                    count += 1
                else:
                    count += 2

        if count > limit:
            arr.append(power)
        else:
            arr.append(count)

    return sum(arr)
def solution(prices):
    sec = []

    for i in range(len(prices)):
        ct = 0

        for k in range(i + 1, len(prices)):
            ct += 1

            if prices[i] > prices[k]:
                break

        sec.append(ct)
    return sec
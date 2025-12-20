if __name__ == '__main__':
    n = int(input())
    bmi = []
    result = [i * 0 for i in range(n)]
    ct = 0

    for _ in range(n):
        w, h = map(int, input().split())
        bmi.append((w, h))

    for i in range(len(bmi)):
        key, value = bmi[i]
        a = 1
        for j in range(len(bmi)):
            if key < bmi[j][0] and value < bmi[j][1]:
                a += 1
        result[ct] += a
        ct += 1

    for i in result :
      print(i, end = " ")
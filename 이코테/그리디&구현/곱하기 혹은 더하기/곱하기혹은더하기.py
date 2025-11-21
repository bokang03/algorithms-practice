if __name__ == '__main__' :
    num = input()
    result = int(num[0])

    for i in range(1, len(num)):
        i = int(num[i])
        if result + i > result * i:
            result += i
        else: result *= i

    print(result)

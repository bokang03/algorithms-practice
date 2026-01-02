if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    calculator_num = [0]
    a = 0
    result = []
    for i in range(n):
        a += nums[i]
        calculator_num.append(a)


    for i in range(n-m+1):
        result.append(calculator_num[m+i] - calculator_num[i])

    print(max(result))
def solution(n):
    # 1 : 1, - 1
    # 2: 1 1, 2, - 2
    # 3: (1 1 1), (1 2), (2, 1) - 3
    # 4 : (1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2) -5
    # 5 : (1,1,1,1,1), (1,1,1,2), (1,1,2,1), (1,2, 1, 1) (2,1,1,1), (2,2, 1), (1, 2, 2)(2, 1, 2)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:

        arr = [-1 for _ in range(n + 1)]
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2

        for i in range(3, len(arr)):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[n] % 1234567
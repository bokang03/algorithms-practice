
if __name__ == '__main__':
    arr = []

    for _ in range(3):
        p, y, name = input().split()
        arr.append((int(p), int(y), name))

    result_num = ''
    for p, y, name in sorted(arr, key=lambda x: x[1]):
        result_num += str(y)[2:]

    result_name = ''
    for p, y, name in sorted(arr, key=lambda x: -x[0]):
        result_name += name[0]

    print(result_num)
    print(result_name)
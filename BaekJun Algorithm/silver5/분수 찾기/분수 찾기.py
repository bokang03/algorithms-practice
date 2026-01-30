if __name__ == "__main__":
    n = int(input())

    line = 1
    while line < n:
        n -= line
        line += 1

    if line % 2 == 0:
        x = n
        y = line - n + 1
    else:
        x = line - n + 1
        y = n

    print(f"{x}/{y}")

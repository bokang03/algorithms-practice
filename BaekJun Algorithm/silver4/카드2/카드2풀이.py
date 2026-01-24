import sys

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())

    ct = 1

    while True :
        if n == 1  :
            print(1)
            break

        if n <= 2** ct :
            print((n - 2**ct//2) * 2)
            break

        ct += 1
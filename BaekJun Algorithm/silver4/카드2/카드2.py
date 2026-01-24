import sys

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    ct = 1
    result = 0

    if  n == 1 :
        print(1)
    else :
        while True :
            if n <= 2 ** ct :
                result, ct = 2**ct, 2**ct

                while True :
                    if ct == n :
                        print(result)
                        break
                    result -= 2
                    ct -= 1
            else :
                ct += 1

            if result != 0 :
                break

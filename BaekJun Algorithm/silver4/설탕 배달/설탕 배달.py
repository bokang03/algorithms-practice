import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    ct = 0
    while True :
        if n%5 == 0 :
           ct += n//5
           break
        n -=  3
        ct += 1
        if n < 0 :
            ct = -1
            break
    print(ct)
import sys

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    arr = set(map(int, input().split()))
    num = int(input())

    ct = 0

    for i in arr :
        if num - i in arr :
            ct +=1
    print(ct//2)
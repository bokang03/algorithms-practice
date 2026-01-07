import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    arr1 = set(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    result = dict()

    for i in arr2 :
        if i in arr1 :
            print(1)
        else : print(0)

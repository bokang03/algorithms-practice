from bisect import  bisect_left, bisect_right
import sys
if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    validate = list(map(int, input().split()))

    arr.sort()

    for i in validate :
        print(bisect_right(arr, i) - bisect_left(arr,i), end = " ")
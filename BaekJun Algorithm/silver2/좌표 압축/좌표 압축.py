from bisect import bisect_left
import sys
if __name__ == '__main__' :
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = list(set(arr))
    arr_set.sort()

    result = [0] * n

    for i in arr :
        print(bisect_left(arr_set, i), end = ' ')


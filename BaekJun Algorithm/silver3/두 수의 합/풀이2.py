import sys

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    num = int(input())

    arr.sort()
    left, right = 0, n-1
    ct = 0

    while left < right :
        if arr[left] + arr[right] == num :
            right -= 1
            ct += 1
        elif arr[left] + arr[right] < num :
            left += 1
        else :
            right -= 1

    print(ct)
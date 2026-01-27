import sys

if __name__ == '__main__' :
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    unduplicated_arr = sorted(set(arr))

    d = {}
    for idx, num in enumerate(unduplicated_arr):
        d[num] = idx

    result = [d[num] for num in arr]

    print(" ".join(map(str, result)))
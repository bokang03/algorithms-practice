import sys
if __name__ == '__main__' :
    input = sys.stdin.readline

    n, m = map(int, input().split())

    arr = set()
    ct = 0

    for _ in range(n) :
        arr.add(input())

    for _ in range(m):
        msg = input()
        if msg in arr :
            ct += 1
    print(ct)
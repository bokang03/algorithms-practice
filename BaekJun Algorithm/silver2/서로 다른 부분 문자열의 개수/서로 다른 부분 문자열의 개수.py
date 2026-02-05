import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    arr = input()
    result = set()

    for i in range(len(arr)):
        limit = i+1
        for k in range(len(arr) - (i+1)) :
            result.add(arr[k:k+i+1])

    print(len(list(result)))


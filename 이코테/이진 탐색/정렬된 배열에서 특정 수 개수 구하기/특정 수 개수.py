from bisect import bisect_left, bisect_right

def ct(arr, x):
    min_index = bisect_left(arr, x)
    max_index = bisect_right(arr, x)
    return max_index - min_index

if __name__ == '__main__':
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    result = ct(arr, x)

    if result == 0 :
        print(-1)
    else : print(result)


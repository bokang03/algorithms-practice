
if __name__ == '__main__' :

    def binary_search(arr, target, st, end) :
        if st > end :
            return None
        mid = (st + end)//2
        if arr[mid] == target :
            return mid
        elif arr[mid] > target :
            return binary_search(arr, target, st, mid-1)
        else :
            return binary_search(arr, target, mid+1, end)

    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    result = binary_search(arr, target, 0, n-1)

    if result == None :
        print("해당 원소 없음")
    else :
        print(result+1)
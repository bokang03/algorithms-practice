
if __name__ == '__main__' :

    def binary_search(arr, target, st, end) :
        while st <= end :
            mid = (st + end)//2

            if arr[mid] == target :
                return mid

            elif arr[mid] > target :
                end = mid-1
            else :
                st = mid + 1
        return None

    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    result = binary_search(arr, target, 0, n-1)

    if result == None :
        print("해당 원소 없음")
    else :
        print(result+1)
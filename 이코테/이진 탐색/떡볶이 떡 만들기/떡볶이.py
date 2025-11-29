
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = 0
    end = max(arr)

    while(st <= end):
        total = 0
        mid = (st+end)//2

        for i in arr :
            if i > mid :
                total += i - mid
        if total < m :
            end = mid - 1
        else :
            result = mid
            st = mid + 1

    print(result)


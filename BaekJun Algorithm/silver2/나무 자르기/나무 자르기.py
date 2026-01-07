
if __name__ == '__main__':
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))


    st, end = 0, max(trees)
    result = 0
    while st <= end :
        total = 0
        mid = (st + end)//2

        for tree in trees :
            if tree > mid :
                total += tree - mid

        if total < m :
            end = mid - 1
        else :
            result = mid
            st = mid + 1


    print(result)


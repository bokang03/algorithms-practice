
if __name__ == "__main__":
    char1 = input()
    char2 = input()

    arr1 = dict()
    arr2 = dict()
    ct = 0

    for i in char1 :
        if i not in arr1 :
            arr1[i] = 1
        else :
            arr1[i] += 1

    for i in char2 :
        if i not in arr2 :
            arr2[i] = 1
        else :
            arr2[i] += 1

    for k, v in arr1.items() :
        if k not in arr2 :
            ct += v
        else :
            if arr2[k] > v :
                ct += arr2[k]-v
                arr2[k] = v
            elif arr2[k] <= v :
                ct += v-arr2[k]
                arr2[k] = v

    for k, v in arr2.items() :
        if k not in arr1 :
            ct += v
        else :
            if arr1[k] > v :
                arr1[k] = v
                ct += arr1[k]-v
            elif arr1[k] <= v :
                arr1[k] = v
                ct += v-arr1[k]
    print(ct)
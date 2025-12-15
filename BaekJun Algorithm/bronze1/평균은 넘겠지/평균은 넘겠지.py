
if __name__ == '__main__':
    n = int(input())
    result = []

    for i in range(n) :
        ct = 0 # 평균을 넘는 사람
        arr = list(map(int, input().split()))
        num = len(arr) # 인원
        avg = sum(arr[1:num])/arr[0] # 평균
        for k in range(1, num):
            if arr[k] > avg :
                ct += 1
        avg_st = round((ct/(num-1)) * 100,3)
        result.append(avg_st)

    for i in result :
        print(str(i) + "%")

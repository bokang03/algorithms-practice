def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    ct = 0
    answer = []
    none_num = lottos.count(0)
    for num in win_nums :
        if num in lottos :
            ct += 1
    result = [none_num + ct, ct]
    for i in result :
        if i == 6 :
            answer.append(1)
        elif i == 5 :
            answer.append(2)
        elif i == 4 :
            answer.append(3)
        elif i == 3 :
            answer.append(4)
        elif i == 2 :
            answer.append(5)
        else :
            answer.append(6)
    return answer

if __name__ == '__main__':
    lottos = list(map(int, input().split()))
    win_nums = list(map(int, input().split()))
    solution(lottos, win_nums)

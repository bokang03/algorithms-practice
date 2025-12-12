def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 맞춘 숫자에 해당하는 순위를 나타내는 배열

    cnt_0 = lottos.count(0)  # 안보이는 숫자 개수
    ans = 0 # 보이는 숫자 중 맞춘 숫자 개수
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]  # 최고 순위, 최소 순위

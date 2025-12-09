def solution(nums):
    answer = 0
    set_num = set(nums)
    if len(set_num) >= len(nums)//2 :
        answer = len(nums)//2
    else :
        answer = len(set_num)
    return answer

if __name__ == '__main__' :
    nums = list(map(int, input().split()))
    print(solution(nums))
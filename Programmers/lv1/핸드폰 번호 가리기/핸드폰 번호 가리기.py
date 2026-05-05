def solution(phone_number):
    fillter_num = len(phone_number) - 4
    arr = ["*" for _ in range(fillter_num)]
    return  "".join(arr) + phone_number[fillter_num:]
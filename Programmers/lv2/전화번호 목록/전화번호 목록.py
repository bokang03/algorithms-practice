def solution(phone_book):
    phone_num = {}

    for num in phone_book:
        phone_num[num] = 1

    for nums in phone_book:
        number = ""
        for num in nums:
            number += num
            if number in phone_num and number != nums:
                return False
    return True

if __name__ == '__main__' :
    arr = ["12","123","1235","567","88"]
    solution(arr)
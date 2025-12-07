def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)


if __name__ == "__main__" :
    # 아래는 테스트로 출력해 보기 위한 코드입니다.
    print("결과 : {}".format(sum_digit(123)))
message = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  # 크로아티아 알파벳
count = len(message)  # 기본 알파벳 개수

for croa in croatia:  # 차례대로 자릿수를 확인한다.
    # IF 6자리 입력 시, c= 은 2자리 이므로 6 -2 = 4 0번 째부터 4자리까지 2자리씩 확인.
    limit = len(message) - len(croa) + 1
    for k in range(limit):
        if message[k: k + len(croa)] in croa:
            # dz=, z= 의 중복을 고려한다.
            if croa == 'dz=':
                count -= (len(croa) - 2)
            else:
                count -= (len(croa) - 1)

print(count)
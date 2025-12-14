def solution(new_id):
    id_swap = []
    for i in new_id:  # 1단계
        if i.isupper():
            id_swap.append(i.swapcase())
        else:
            id_swap.append(i)

    id = []
    id_guide = ["-", "_", "."]
    for i in id_swap:  # 2단계
        if i in id_guide:
            id.append(i)
        elif i.islower() == True:
            id.append(i)
        elif i.isdigit() == True:
            id.append(i)

    comma = ""
    id_3 = []
    for i in range(len(id)):  # 3단계
        if id[i] == ".":
            if comma != ".":
                comma = id[i]
                id_3.append(id[i])
                continue
        else:
            id_3.append(id[i])
            comma = id[i]

    while len(id) > 0:  # 4단계
        if id_3[0] == ".":
            del id_3[0]
            if len(id_3) == 0: break

        if id_3[-1] == ".":
            del id_3[-1]
            if len(id_3) == 0: break

        if id_3[0] != "." and id_3[-1] != ".":
            break

    if len(id_3) == 0:  # 5단계
        id_3.append("a")
    elif len(id_3) >= 16:  # 6단계
        id_3 = id_3[:15]
        while True:
            if id_3[-1] == ".":
                del id_3[-1]
            else:
                break

    if len(id_3) <= 2:  # 7단계
        while len(id_3) < 3:
            id_3.append(id_3[-1])

    result = ""
    for i in id_3:
        result += i
    return result

if __name__ == '__main__':
    new_id = input()
    print(solution(new_id))
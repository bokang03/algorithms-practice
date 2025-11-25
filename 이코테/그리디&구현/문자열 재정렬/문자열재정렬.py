if __name__ == '__main__' :
    input_data = input()
    num = 0
    str_arr = []

    for i in range(len(input_data)) :
        data = input_data[i]
        if data.isdigit() == True :
            num += int(data)
        else : str_arr.append(data)

    str_arr.sort()
    str_arr.append(str(num))
    print(''.join(str_arr))

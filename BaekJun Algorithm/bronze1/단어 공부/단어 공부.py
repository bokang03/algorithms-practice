

if __name__ == "__main__" :

    msg = input()
    result = dict()
    answer = []

    for i in msg :
        if i.isupper() :
             i = i.lower()
        if i in result :
              result[i] += 1
        else : result[i] = 1

    ct = 0

    for a, num in result.items() :
        answer.append(num)



    if answer.count(max(answer)) > 1 :
        print("?")
    else :
        for a, num in result.items() :
            if num == max(answer) :
                print(a.upper())
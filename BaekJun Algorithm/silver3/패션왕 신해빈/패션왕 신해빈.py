
if __name__ == '__main__':

    for i in range(int(input())):
        fashion = dict()
        ct = 1
        # 단독 의류  + (n * k) + (n * p)
        for k in range(int(input())):
            name, clothing = input().split()
            if clothing not in fashion :
                fashion[clothing] = [name]
            else :
                fashion[clothing].append(name)
        for i in fashion.values() :
            ct *= (len(i) + 1)
        print(ct - 1)
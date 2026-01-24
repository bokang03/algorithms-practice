
if __name__ == "__main__":
    n1, n2 = map(int, input().split())
    min_num = 0

    for i in range(1, min(n1, n2)+1) :
        if n1%i == 0 and n2%i == 0 :
            min_num = i

    max_num = (n1 * n2)//min_num

    print(min_num)
    print(max_num)
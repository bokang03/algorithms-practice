if __name__ == '__main__':
    n = int(input())
    wood = [1, 2, 4, 8, 16, 32, 64]
    ct = 0

    def a(w, ct) :
        ct += 1
        wood.append(w)
        wood.sort()
        if wood.count(w) > 1 :
            print(ct)
            return ct
        else :
            result = w - wood[wood.index(w) - 1]
            a(result, ct)
            return ct


    a(n, ct)
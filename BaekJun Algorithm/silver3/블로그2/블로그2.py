
if __name__ == '__main__':
    n = int(input())
    c = input()
    colors = {"B" : 0, "R" : 0}
    colors[c[0]] += 1

    for i in range(1, n):
        if c[i] != c[i-1] :
            colors[c[i]] += 1

    result = min(colors["B"], colors["R"]) + 1
    print(result)
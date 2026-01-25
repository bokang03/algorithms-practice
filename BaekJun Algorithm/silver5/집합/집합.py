import sys
if __name__ == '__main__' :
    input = sys.stdin.readline
    graph = set()
    for _ in range(int(input())) :
        comm = list(map(str, input().split()))

        if comm[0] == "add" :
            graph.add(int(comm[1]))

        elif comm[0] == "remove" :
            if int(comm[1]) in graph :
                graph.remove(int(comm[1]))
            else :
                continue

        elif comm[0] == "check" :
            if int(comm[1]) in graph :
                print(1)
            else :
                print(0)

        elif comm[0] == "toggle" :
            if int(comm[1]) in graph :
                graph.remove(int(comm[1]))
            else :
                graph.add(int(comm[1]))

        elif comm[0] == "all" :
            graph = set(i for i in range(1, 21))
        elif comm[0] == "empty" :
            graph.clear()
a, b, c = map(int, input().split())
array = []
n = []
result = 0


for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            array.append(i+j+k)

result = max(array)

for i in range(3, result+1):
    result = array.count(i)
    n.append(result)

print(n.index(max(n))+3)
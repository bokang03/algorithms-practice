x = int(input())
guest = list(map(int, input().split()))
result = 0

for i in range(1, 101):
    if guest.count(i) > 1:
        result += guest.count(i) - 1
      
print(result)
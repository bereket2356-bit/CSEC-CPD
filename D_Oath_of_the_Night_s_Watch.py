n = int(input())
a = list(map(int, input().split()))
min = min(a)
max = max(a)
count = 0
for x in a:
    if x != min and x != max:
        count += 1
print(count)

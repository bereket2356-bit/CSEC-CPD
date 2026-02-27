t = int(input())
x="Timur"
for _ in range(t):
    n = int(input())
    s=input()
    if sorted(s)==sorted(x):
        print("YES")
    else:
        print("NO")
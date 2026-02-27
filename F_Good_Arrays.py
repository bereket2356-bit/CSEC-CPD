t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    if n == 1:
        print("NO")
    elif all(x == 1 for x in a):
        print("NO")
    else:
        print("YES")
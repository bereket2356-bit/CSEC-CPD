t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    
    power = 10
    while power <= n:
        d = power + 1
        if n % d == 0:
            ans.append(n // d)
        power *= 10
    
    if not ans:
        print(0)
    else:
        ans.sort()
        print(len(ans))
        print(*ans)

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    pos = p.index(n)
    
    if pos != 0:
        p = p[:pos+1][::-1] + p[pos+1:]
    else:
        pos2 = p.index(n-1)
        p = [p[0]] + p[1:pos2+1][::-1] + p[pos2+1:]
    
    print(*p)

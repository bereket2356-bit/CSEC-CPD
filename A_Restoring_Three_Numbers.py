x1,x2,x3,x4=list(map(int,input().split()))
s=sorted([x1,x2,x3,x4])
print(s[3]-s[2],s[3]-s[1],s[3]-s[0])
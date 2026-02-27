n=int(input())
count=9
l=1
s=1
if n<count:
    print(n)
else:
    while count<n:
        l+=1
        s+=1
        count+=s*8
    print(l)
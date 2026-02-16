n=int(input())
count=0
s=input()
for j in range(n-1):
    if s[j]==s[j+1]:
        count+=1            
print(count)    
 

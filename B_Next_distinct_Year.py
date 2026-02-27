y=int(input())
n_str=str(y)
unique=set(n_str)
while len(unique)<=4:
    y+=1
    n_str=str(y)
    unique=set(n_str)
    if len(unique)==4:
        break
print(y)
t = int(input())

for _ in range(t):
    n = input()
    length = len(n)
    result = []
    
    for i in range(length):
        if n[i] != '0':
            round_number = n[i] + '0' * (length - i - 1)
            result.append(round_number)
    
    print(len(result))
    print(*result)
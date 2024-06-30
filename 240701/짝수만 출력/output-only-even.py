a, b = input().split()
result = int(a)
while result <= int(b):
    if result % 2 == 0:
        print(result, end=' ')
        result += 1
    else:
        result += 1
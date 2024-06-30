a, b = input().split()

for i in range(int(a), int(b)-1, -1):
    if i % 2 == 1:
        print(i, end=' ')
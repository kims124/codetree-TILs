x=input()
x=x.split()
h = int(x[0])
w = int(x[1])
bmi = w/(h*h)
if int(bmi*10000) >= 25:
    print(int(bmi*10000))
    print("Obesity")
else:
    print(int(bmi*10000))
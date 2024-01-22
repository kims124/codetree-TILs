A = 0
x = input()
x=x.split()
if x[0] == "Y" and  int(x[1])>=37:
    A +=1    
y = input()
y=y.split()
if y[0] == "Y" and  int(y[1])>=37:
    A +=1    
z = input()
z=z.split()
if z[0] == "Y" and  int(z[1])>=37:
    A +=1    

if A >= 2:
    print("E")
else:
    print("N")
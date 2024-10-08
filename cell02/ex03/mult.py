x = int(float(input("Enter first number:")))
y = int(float(input("Enter second number:")))

Num = x * y

print(x , "x" , y , "=" , Num)

if Num > 0:
    print("This number is positive.")
elif Num == 0:
    print("This number is both positive and negitive")
else:
    print("This number is negitive")
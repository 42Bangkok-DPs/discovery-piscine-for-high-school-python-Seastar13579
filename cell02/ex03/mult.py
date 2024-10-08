#!/usr/bin/env python3

x = input ("Enter first number:")
y = input ("Enter second number:")

x = int (x)
y = int (y)

Num = (x * y)

print (x , "x" , y , "=" , Num)

if Num > 0:
    print ("This number is positive.")
elif Num == 0:
    print ("This number is both positive and negitive")
else:
    print ("This number is negitive")
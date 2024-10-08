#!/usr/bin/env python3

Num = int(input("Enter a number less than 25:"))
if Num < 26:
    while Num < 26:
        print ("Inside the loop, my variable is",Num)
        if Num == 26:
            break
        Num += 1
else:
    print ("Error")
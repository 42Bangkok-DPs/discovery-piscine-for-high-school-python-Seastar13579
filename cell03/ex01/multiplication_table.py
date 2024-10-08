#!/usr/bin/env python3

Num = int(input("Enter a number:"))
number = 0
while number < 13:
    res = Num * number
    print(number,"x",Num,"=",res)
    if number == 13:
            break
    number += 1
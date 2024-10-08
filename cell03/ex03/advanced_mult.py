#!/usr/bin/env python3

x = 0
def func1():
    y = 0
    while y <= 10:
        res = x * y
        print(res,end=" ")
        y += 1
while x <= 10:
    print("Table de",x, ":",end=" ")
    func1()
    x += 1
    print()

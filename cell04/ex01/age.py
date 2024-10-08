#!/usr/bin/env python3

Age = int(input("Tell me your age:"))
print("You are currently",Age,"years old.")
z = 0
while z < 25:
    z += 10
    Age += 10
    print("In",z,"years, you'll be",Age,"years old.")
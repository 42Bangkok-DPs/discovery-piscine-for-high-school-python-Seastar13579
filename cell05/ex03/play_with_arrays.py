#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2]
b = [Num + 2 for Num in a]
c = [Num for Num in b if Num > 5]

set1 = set(c)

print (a)
print(set1)
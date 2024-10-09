#!/usr/bin/env python3

import sys

no = ("None")
code = ("Code1")
x = (len(sys.argv)-1)

if x <= 0:
    print(no)
else:
    print(sys.argv[1])
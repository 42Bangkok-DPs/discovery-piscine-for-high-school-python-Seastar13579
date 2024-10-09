#!/usr/bin/env python3

import sys

x = (len(sys.argv)-1)

if x == 1:
    check = (sys.argv[-1])
    usrin = input("What was the parameter?:")
    if usrin == check:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
#!/usr/bin/env python3

import sys

x = (len(sys.argv)-1)

if x <= 1:
    print("none")
else:
    usrin = (sys.argv[1:])
    for o in reversed(usrin):
        print (o)
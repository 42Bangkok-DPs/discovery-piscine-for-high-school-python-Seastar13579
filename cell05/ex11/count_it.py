#!/usr/bin/env python3

import sys

x = (len(sys.argv)-1)

if x >= 1:
    for y in (sys.argv[1:]):
        print(y + ":",len(y))
else:
    print("none")
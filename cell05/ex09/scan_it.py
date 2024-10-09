#!/usr/bin/env python3

import sys
import re

#put ()infront of len
x = (len(sys.argv)-1)

if x == 2:
    scan = (sys.argv[1])
    word = (sys.argv[2])
    x = re.findall(scan,word)
    y = len(x)
    if y <= 0:
        print("none")
    else:
        print(y)
    
else:
    print("none")
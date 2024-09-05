#!/usr/bin/env python3
import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

with open("/csvserver/inputFile", 'w') as f:
    for i in range(start, end + 1):
        f.write(f"{i}, {random.randint(1, 500)}\n")

print(f"Generated inputFile with entries from {start} to {end}.")
import sys
import math
A, B, V = map(int, sys.stdin.readline().split())

day = math.ceil(V - B / A - B)
print (day)

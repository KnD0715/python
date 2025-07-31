import sys

num1, num2 = map(int, sys.stdin.readline().split())

reversed_num1 = int(str(num1)[::-1])
reversed_num2 = int(str(num2)[::-1])

if reversed_num1 > reversed_num2:
    print (reversed_num1)

else:
    print (reversed_num2)

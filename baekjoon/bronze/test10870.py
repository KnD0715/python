import sys

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

num = int(sys.stdin.readline())
print (fibonacci(num))


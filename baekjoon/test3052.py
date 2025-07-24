import sys
numbers = []

for i in range (10):
    num = int(sys.stdin.readline())
    result = num % 42
    numbers += [result]

remainder_number = list(set(numbers))

print (len(remainder_number))
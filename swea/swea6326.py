def factorial(n):
    while n < 1:
        return 1
    result = 0
    result += n * factorial(n - 1)
    return result

number = int(input())

print (factorial(number))
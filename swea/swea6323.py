def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci (num - 2)

number = int(input())
fibo_list = []

for i in range (1, number + 1):
    result = fibonacci(i)
    fibo_list += [result]

print (fibo_list)
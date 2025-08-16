num_list = [num for num in range(1, 21) if num % 3 != 0 or num % 5 != 0]

result = []
for num in num_list:
    result.append(num ** 2)

print(result)
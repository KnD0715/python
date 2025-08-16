num_list = list(map(int, input().split(',')))

result = [num for num in num_list if num % 2 != 0]

print(', '.join(map(str, result)))
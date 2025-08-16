num_list = [12, 24, 35, 70, 88, 120, 155]

result = [num_list[i] for i in range(len(num_list)) if i == 1 or i == 2 or i == 3 or i == 6]

print(result)
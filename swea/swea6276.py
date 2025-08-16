result = []

for i in range(2, 10):
    num_list = []
    if i % 3 != 0 and i % 7 != 0:
        for j in range(1, 10):
            if j % 3 != 0 and j % 7 != 0:
                num_list.append(i * j)

    result.append(num_list)

print(result)
my_list = []
for i in range (100, 301):
    if (i // 100 % 2 == 0 and i // 10 % 2 == 0 and i % 2 == 0):
        my_list.append(str(i))

print (','.join(my_list))
num = input()
my_list = [0] * 10

for char in num:
    my_list[int(char)] += 1

print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(' '.join(str(c) for c in my_list))
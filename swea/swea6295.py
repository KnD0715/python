a = input()
num_list = list(map(int, a.split(',')))
result = [[i * j for i in range(int(num_list[1]))] for j in range(int(num_list[0]))]
print(result)

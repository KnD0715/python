my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x : x % 2 == 0, my_list))
pow_list = list(map(lambda x : x ** 2, even_list))

print (pow_list)
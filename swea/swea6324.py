def deduplication_list(my_list):
    de_list = list(set(my_list))
    return de_list

my_list = [1, 2, 3, 4, 3, 2, 1]
print (my_list)
print (deduplication_list(my_list))
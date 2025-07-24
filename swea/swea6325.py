def find_number (num):
    global my_list
    for number in my_list:
        if number == num:
            print (f"{num} => True")
            break
    else:
        print (f"{num} => False")
    

my_list = [2, 4, 6, 8, 10]
print (my_list)
find_number(5)
find_number(10)
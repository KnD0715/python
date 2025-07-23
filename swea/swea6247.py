num = 4
blank_num = 0

while num > 0:
    while blank_num < 4:
        blank = ' ' * blank_num
        star = '*' * (num * 2 - 1)
        num -= 1
        blank_num += 1
        print (blank + star)
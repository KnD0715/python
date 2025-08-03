def pow_num(*args):
    score = 1
    try:
        for i in args:
            score *= int(i)
    except TypeError:
        return ('에러발생')
    
    return score

my_list = [1, 2, 'a', 3]
print (pow_num(my_list))
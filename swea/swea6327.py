def pow(num1, num2):
    pow_num1 = num1 * num1
    pow_num2 = num2 * num2
    print (f"square({num1}) => {pow_num1}")
    print (f"square({num2}) => {pow_num2}")

num1, num2 = map(int, input().split(', '))
pow(num1, num2)
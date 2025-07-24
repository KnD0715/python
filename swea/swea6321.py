def prime_number(num):
    for i in range (2, num):
        if num % i == 0:
            break
    
    else:
        print("소수입니다.")

num = int(input())
prime_number(num)
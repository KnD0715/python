T = int(input())

for i in range(T):
    alphabet = str(input())

    if (alphabet.islower()):
        result = "소문자"
    else:
        result = "대문자"
    
    print ('#%d %s 는 %s 입니다.' % (i + 1, alphabet, result))
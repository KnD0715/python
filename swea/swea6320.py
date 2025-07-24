def rock_scissors_paper(person1, person2):
    if person1 == '가위':
        if person2 == '가위':
            print ("비겼습니다!")
        elif person2 == '바위':
            print ('바위가 이겼습니다!')
        elif person2 == '보':
            print ('가위가 이겼습니다!')
    
    elif person1 == '바위':
        if person2 == '가위':
            print ("바위가 이겼습니다!")
        elif person2 == '바위':
            print ('비겼습니다!')
        elif person2 == '보':
            print ('보가 이겼습니다!')
    
    elif person1 == '보':
        if person2 == '가위':
            print ("가위가 이겼습니다!")
        elif person2 == '바위':
            print ('보가 이겼습니다!')
        elif person2 == '보':
            print ('비겼습니다!')

person1 = input()
person2 = input()
match1 = input()
match2 = input()
rock_scissors_paper(match1, match2)

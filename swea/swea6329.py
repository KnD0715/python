def countdown(num):
    if num <= 0:
        print (f"카운트다운을 하려면 {num}보다 큰 입력이 필요합니다.")

    for i in range (num, 0, -1):
        print (i)

countdown(0)
countdown(10)
T = int(input())    # 테스트 케이스 설정

for i in range(1, T + 1):   # 테스트 케이스 수만큼 반복
    two = 0
    three = 0
    five = 0
    seven = 0
    eleven = 0
    num = int(input())  # 숫자 입력

    while num > 1:  # 몫이 1이 될 때까지 반복
        if num % 11 == 0:
            eleven += 1
            num //= 11
            continue

        elif num % 7 == 0:
            seven += 1
            num //= 7
            continue

        elif num % 5 == 0:
            five += 1
            num //= 5
            continue

        elif num % 3 == 0:
            three += 1
            num //= 3
            continue

        elif num % 2 == 0:
            two += 1
            num //= 2
            continue

    print(f"#{i} {two} {three} {five} {seven} {eleven}")

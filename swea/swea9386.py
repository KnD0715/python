N = int(input())    # 테스트 케이스 입력

for i in range(1, N + 1):
    length = int(input())   # 수열 길이 입력
    num = input()   # 수열 입력
    max_count = 0
    count = 0
    for j in num:
        if j == '1':
            count += 1  # 수열의 숫자가 1일 시 카운트 증가
            if max_count < count:
                max_count = count   # 최댓값 추출

        else:   # 수열의 숫자가 0일 시 카운트 초기화
            count = 0
    
    print(f"#{i} {max_count}")
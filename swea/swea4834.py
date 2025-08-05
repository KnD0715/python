T = int(input())    # 테스트 케이스 입력

for i in range(1, T + 1):   # 테스트 케이스만큼 반복
    N = int(input())    # 카드 장수 입력
    card = int(input()) # 카드 숫자 공백없이 입력
    card_count_list = [0] * 10  # 0 ~ 9까지 카드 리스트 생성
    for count in range(N):  # 카드 장수만큼 반복
        card_count_list[card % 10] += 1 # 카트 숫자를 10으로 나눈 나머지를 카드 리스트에 추가
        card //= 10 # 카드 숫자를 10으로 나눈 몫

    max_num = 0 # 최대값 인덱스 초기 설정
    for num in range(len(card_count_list)): # 카드 리스트 수만큼 반복
        if card_count_list[max_num] < card_count_list[num]: # 많은 카드의 개수 찾기
            max_num = num

        if card_count_list[max_num] == card_count_list[num]:    # 만약 카드의 개수가 같다면 높은 값 설정
            max_num = num   # 0 ~ 9까지의 인덱스이기 때문

    print(f"#{i} {max_num} {card_count_list[max_num]}")

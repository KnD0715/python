T = int(input()) # 테스트 케이스 입력

for _ in range(1, T + 1):
    box = int(input())  # 박스 개수 입력
    box_list = list(map(int, input().split()))  # 박스 리스트 입력
    max_count = 0  # 낙차 최대 수 초기 설정
    for i in range(box):    # 박스 수만큼 반복문
        count = 0   # 낙차 수 초기 설정
        for j in range(i + 1, box): # box_list[i]의 다음 인덱스부터 박스 수까지 반복문
            if box_list[i] > box_list[j]:   # box_list[i]의 값이 box_list[j]의 값보다 크면 카운트 증가
                count += 1

            if max_count < count:
                max_count = count

    print(f"#{_} {max_count}")

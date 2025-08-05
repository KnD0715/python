T = int(input())    # 테스트 케이스 출력

for i in range(1, T + 1):   # 테스트 케이스 수만큼 반복
    max_move, route, charge_station_num = map(int, input().split()) # 최대 이동수, 정류장 수, 충전소 수 입력
    bus_stop = [0 for _ in range(route + 1)]    # 정류장 수만큼 버스 정류장 리스트 생성
    charge_station = list(map(int, input().split()))    # 충전소 위치 입력

    for num in charge_station:  # 충전수 수만큼 반복문
        bus_stop[num] += 1  # 충전소에 위치 값에 버스 정류장 리스트 1 증가

    now = count = 0 # 현재 위치와 카운트 값 초기 설정
    move = now + max_move   # 현재 위치와 최대 이동수 더한 값

    while move < route: # 이동 위치가 정류장 수를 넘을때까지 반복
        if bus_stop[move] == 1: # 이동 위치에 1이 있다는 것은 충전소가 있다는 뜻
            now = move  # 이동 위치를 현재 위치로 재설정
            move = now + max_move   # 이동 위치 재설정
            count += 1  # 카운트 증가

        else:   # 이동 위치에 1이 아니라는 것은 충전소가 없다는 뜻
            move -= 1   # 뒤로 한 칸 가기
            if now == move: # 만약 현재 위치가 이동 위치와 같아진다면 그 구간동안
                count = 0   # 충전소가 없기에 0 반환
                break

    print(f"#{i} {count}")

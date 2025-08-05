T = int(input())  # 테스트 케이스 입력
for i in range(1, T + 1):  # 테스트 케이스 수만큼 반복
    N = int(input())
    bus = [0] * 5001  # 버스 정류장 5000개 만듬
    for _ in range(N):  # N만큼 반복
        a, b = map(int, input().split())  # A, B 입력
        for j in range(a, b + 1):
            bus[j] += 1  # A부터 B까지 버스 정류장 1 증가

    P = int(input())
    result = [] # 반환할 리스트 생성

    for _ in range(P):  # P만큼 반복
        result.append(bus[int(input())])    # 입력하는 버스 정류장을 반환할 리스트에 저장

    print(f"#{i}", *result)

import sys
sys.stdin = open('input_18123.txt')

T = int(input())    # 테스트 케이스 입력

for _ in range(1, T + 1):   # 테스트 케이스만큼 반복
    N = int(input())    # 배열 길이 입력
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 생성
    result = 0  # 결과 값 초기 설정
    circuit_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]    # 이웃한 요소 값 구할 때 쓸 리스트 생성
    for i in range(N):  # 행 길이만큼 반복
        for j in range(N):  # 열 길이만큼 반복
            for di, dj in circuit_arr:  # 이웃한 요소 값을 추출
                num = 0
                ni, nj = i + di, j + dj # 행과 열값을 더한 값을 새로운 값으로 생성
                if 0 <= ni < N and 0 <= nj < N: # 행과 열의 값이 0부터 배열의 길이까지만 코드를 실행
                    num = arr[i][j] - arr[ni][nj]   # 인접한 요소의 차를 구함
                    result += abs(num)  # 인접한 요소의 차의 절대값을 더함
    print(f"#{_} {result}")

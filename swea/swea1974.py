import sys

sys.stdin = open('input_1974.txt')

T = int(input())  # 테스트 케이스 입력
circuit_arr = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]  # 3 X 3 크기의 값을 비교하기 위한 리스트 생성

for i in range(1, T + 1):  # 테스트 케이스만큼 반복
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 배열 생성

    result = 1  # 결과 값 1로 초기 설정
    sudoku_result = 45  # 스도쿠 총합 45로 초기 설정
    for row in range(9):  # 행 길이만큼 반복
        if sudoku_result == 45:  # 스도쿠 총합이 45면
            result = 1  # 결과 값 1로 설정
        else:
            result = 0  # 총합이 45면 결과 값을 0으로 설정 후 반복문 종료
            break

        if result == 0:  # 결과 값이 0이라면 바로 반복문 종료
            break
        sudoku_result = 0  # 스도쿠 총합 0으로 초기화
        for column in range(9):  # 열 길이만큼 반복
            sudoku_result += sudoku[row][column]  # 행 덧셈

    for column in range(9):  # 열 길이만큼 반복
        if sudoku_result == 45:  # 행에서 더한 값 그대로 내려왔기 때문에 45로 설정
            result = 1  # 결과 값 1 유지
        else:  # 만약 결과 값이 45가 아니라면 마지막으로 더한 행 값이 45가 안되기 때문에
            result = 0  # 결과 값 0 수정 후 반복문 종료
            break

        if result == 0:  # 행 값에서 0이 나올 수 있기에
            break  # 코드 실행 안 하고 바로 종료

        sudoku_result = 0  # 모든 검증이 끝나 문제가 없으면 스도쿠 총합 0으로 초기화
        for row in range(9):  # 행 길이만큼 반복
            sudoku_result += sudoku[row][column]  # 열 덧셈

    for row in range(0, 9, 3):  # 행 3칸마다 반복
        if sudoku_result == 45:  # 앞에 기능과 동일
            result = 1
        else:
            result = 0
            break

        if result == 0:
            break
        for column in range(0, 9, 3):  # 열 길이만큼 반복
            if sudoku_result == 45:  # 기능 동일
                result = 1
            else:
                result = 0
                break

            if result == 0:
                break
            sudoku_result = 0
            for square_row, square_column in circuit_arr:  # 3x3 덧셈을 위한 리스트로 반복
                new_row, new_column = row + square_row, column + square_column  # 새로운 행과 열 생성
                sudoku_result += sudoku[new_row][new_column]  # 3x3 덧셈

    print(f"#{i} {result}")

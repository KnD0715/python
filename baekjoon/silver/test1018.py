import sys

correct_chess_start_B = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
correct_chess_start_W = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

row, column = map(int, sys.stdin.readline().split())
chess = [sys.stdin.readline().strip() for _ in range(row)]

result = float('inf')

for i in range(0, row - 7):
    for j in range(0, column - 7):
        count_B = 0
        count_W = 0

        for check_row in range(8):
            for check_column in range(8):
                if correct_chess_start_B[check_row][check_column] != chess[i + check_row][j + check_column]:
                    count_B += 1
                if correct_chess_start_W[check_row][check_column] != chess[i + check_row][j + check_column]:
                    count_W += 1

        if result > count_B:
            result = count_B
        if result > count_W:
            result = count_W

print(result)

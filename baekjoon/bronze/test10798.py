import sys

arr = [list(sys.stdin.readline().strip()) for _ in range(5)]

new_arr = []

for column in range(15):
    for row in range(5):
        if column < len(arr[row]):
            new_arr.append(arr[row][column])

print (''.join(new_arr))
import sys

time = int(sys.stdin.readline())
control = [0, 0, 0]
result = 0

while 10000 >= time > 0:
    if  time >= 300:
        time -= 300
        control[0] += 1

    elif time >= 60:
        time -= 60
        control[1] += 1

    elif time >= 10:
        time -= 10
        control[2] += 1

    elif time < 10:
        result = -1
        break

if result == -1:
    print(result)

else:
    print(*control)
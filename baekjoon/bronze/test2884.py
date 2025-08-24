import sys

h, m = map(int, sys.stdin.readline().split())

min = h * 60 + m - 45

hour = int(min // 60)
minute = int(min % 60)

if (hour < 0):
    hour = 23

print (str(hour) + " " + str(minute))
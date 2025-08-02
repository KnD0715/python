import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

distance1 = x1
distance2 = x2 - x1
distance3 = y1
distance4 = y2 - y1

distance_list = [distance1, distance2, distance3, distance4]

print (min(distance_list))
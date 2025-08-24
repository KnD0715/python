import sys

color_dict = {
    'black' : [0, 1],
    'brown' : [1, 10],
    'red' : [2, 100],
    'orange' : [3, 1000],
    'yellow' : [4, 10000],
    'green' : [5, 100000],
    'blue': [6, 1000000],
    'violet' : [7, 10000000],
    'grey' : [8, 100000000],
    'white' : [9, 1000000000],
}
color_list = []
for i in range(2):
    color = sys.stdin.readline().strip()
    color_list.append(color_dict[color][0])

result = ''
for _ in color_list:
    result += str(_)

color = sys.stdin.readline().strip()
om = int(result) * color_dict[color][1]
print (om)
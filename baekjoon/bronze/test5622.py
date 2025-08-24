import sys

dial_list = {
    3: ['A', 'B', 'C'],
    4 : ['D', 'E', 'F'],
    5 : ['G', 'H', 'I'],
    6 : ['J', 'K', 'L'],
    7 : ['M', 'N', 'O'],
    8 : ['P', 'Q', 'R', 'S'],
    9 : ['T', 'U', 'V'],
    10 : ['W', 'X', 'Y', 'Z'],
}

dial = sys.stdin.readline().strip()

result = 0
for _ in dial:
    for time, letters in dial_list.items():
        if _ in letters:
            result += time
            break

print (result)
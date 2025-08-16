import math

num_list = list(map(int, input().split(', ')))

result = []

for num in num_list:
    result.append(f"{2 * math.pi * num:.2f}")

print(", ".join(result))


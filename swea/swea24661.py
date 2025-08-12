num_list = list(map(int, input().split()))

new_list = []
for i in sorted(num_list):
    if i % 2 != 0:
        new_list.append(i ** 2)

print(*new_list)

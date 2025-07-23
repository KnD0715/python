odd = []

for i in range (1, 101):
    if i % 2 != 0:
        odd.append(str(i))

print(', '.join(odd))
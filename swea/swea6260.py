word = input()

upper_case = 0
lower_case = 0

for ch in word:
    if ch.islower():
        lower_case += 1

    elif ch.isupper():
        upper_case += 1

print(f"UPPER CASE {upper_case}")
print(f"LOWER CASE {lower_case}")
word = input()

letters = 0
digits = 0

for ch in word:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
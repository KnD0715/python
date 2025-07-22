word = str(input())
ascii_val = ord(word)


if (word.islower()):
    word_change = word.upper()
else:
    word_change = word.lower()

ascii_val_change = ord(word_change)

print (f"{word}(ASCII: {ascii_val}) => {word_change}(ASCII: {ascii_val_change})")
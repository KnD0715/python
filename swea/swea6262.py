word = input()

word_count = {ch : word.count(ch) for ch in word}

for key, value in word_count.items():
    print(f"{key},{value}")
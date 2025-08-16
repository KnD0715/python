word = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

word_list = [ch for ch in word if ch not in 'aeiou']

print(''.join(word_list))
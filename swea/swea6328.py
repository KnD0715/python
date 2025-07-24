def long_word(word1, word2):
    word1_list = []
    word2_list = []
    for char in word1:
        word1_list += [char]
    
    for char in word2:
        word2_list += [char]
    
    if (len(word1_list)) > (len(word2_list)):
        print (word1)
    else:
        print (word2)

word1, word2 = input().split(', ')
long_word(word1, word2)
word = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
score_map = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1}

score = sum(map(lambda x : score_map[x], word))
print (score)
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0

while score:
    sc = score.pop(0)
    if sc >= 80:
        result += sc
        
print (result)
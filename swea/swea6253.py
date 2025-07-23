Decimal = int(input())
Binary = ""

while Decimal > 0:
    if (Decimal % 2 == 0):
        Binary += str(0)
    else:
        Binary += str(1)
    
    Decimal = Decimal // 2

Binary = Binary[::-1]

print(Binary)
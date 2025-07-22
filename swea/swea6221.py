Man1 = str(input())
Man2 = str(input())

if (Man1 == "가위"):
    if (Man2 == "바위"):
        Result = "Man2 Win!"
    elif (Man2 == "가위"):
        Result = "Draw"
    elif (Man2 == "보"):
        Result = "Man1 Win!"

elif (Man1 == "바위"):
    if (Man2 == "바위"):
        Result = "Draw"
    elif (Man2 == "가위"):
        Result = "Man1 Win!"
    elif (Man2 == "보"):
        Result = "Man2 Win!"

elif (Man1 == "보"):
    if (Man2 == "바위"):
        Result = "Man1 Win!"
    elif (Man2 == "가위"):
        Result = "Man2 Win!"
    elif (Man2 == "보"):
        Result = "Draw"

print ("Result : %s" % Result)
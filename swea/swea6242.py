Blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
A_count = 0
B_count = 0
AB_count = 0
O_count = 0

for blood in Blood:
    if blood == 'A':
        A_count += 1
    elif blood == 'B':
        B_count += 1
    elif blood == 'O':
        O_count += 1
    elif blood == 'AB':
        AB_count += 1

blood_dict = {'A' : A_count, 'O' : O_count, 'B' : B_count, 'AB' : AB_count}

print(blood_dict)
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

new_beer = {key : values * 1.05 for key, values in beer.items()}
print(f"{beer}")
print(f"{new_beer}")

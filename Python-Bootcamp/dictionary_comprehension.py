cities_in_F = {"New York":32, "Los Angeles":74, "Boston":100}

cities_in_C = {key: round((value -32) *(5/9)) for key, value in cities_in_F.items()}
print(cities_in_C)

#Withought Dictionary comprehension it will look like this

for key, value in cities_in_C.items():
    value = round((value -32) *(5/9))
    print(key, value)
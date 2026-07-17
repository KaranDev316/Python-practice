

j = "f11"
k= "b23"

source_map_2 = dict(zip(j,k))
if len(source_map_2) == len(set(j)) and len(source_map_2) == len(set(k)):
    print(True)
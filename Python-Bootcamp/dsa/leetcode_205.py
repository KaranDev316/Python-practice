

j = "f11"
k= "b23"
longest_string = 0
if len(j) > len(k):
    longest_string = len(j)
else:
    longest_string = len(k)

source_map_2 = dict(zip(j,k))
if len(source_map_2) == longest_string:
    print(True)
else:
    print(False)
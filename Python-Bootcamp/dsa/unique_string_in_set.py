
list1 = ["cat", "dog", "bird"]

seen = set()
duplicate1 = set()

for item in list1:
    if item not in seen:
        seen.add(item)
    else:
        duplicate1.add(item)
for item in list1:
    if item not in duplicate1:
        print(item)
        break
else:
    print("No unique string")


try:
    items = [1, 2, 3]
    print(items[11])  # Triggering an IndexError

except IndexError:
    print("That item is not in the list")
else:
    print("That item is in the list")
animals = ["lion", "tiger", "monkey", "elephant", "frog"]
filtered_animals = []

for animal in animals:
    filtered_animals.append(animal.title())

print(filtered_animals)
# list comprehension version
animals = ["lion", "tiger", "monkey", "elephant", "frog"]
filtered_animals = [animal.title() for animal in animals]
print(filtered_animals)

def greet(name="Guest", **kwargs):
    print(name)
    print(kwargs)

data = {
    "country": "Malawi",
    "city": "Lilongwe"
}

greet("Alfred", **data)
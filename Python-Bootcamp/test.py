
x = 100

def outer():

    x = 50

    def inner():
        nonlocal x
        print(x)

        x = 10

    inner()

outer()
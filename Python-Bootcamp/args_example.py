def get_args(*args):
    print(args)
list1 = []
for i in range(5):
    list1.append("*")
    get_args(list1)
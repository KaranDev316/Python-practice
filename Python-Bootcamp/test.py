#scope in python

def outer():
     x = 10
     def inner():
          def inner_inner():
               return x
          return inner_inner()
     return inner()
result = outer()
print(result)



class User:
    def __init__(self, name,email,password):
        self.name = name
        print(name)
        self.email = email
        self.password = password

    def name(self):
        print(self.name)

user1 = User("alfred","a@gmail.com","123abc")
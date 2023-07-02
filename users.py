from register import Register

class User(Register):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    

# admin = Admin("alireza", "alireza")
# print(admin.user)

class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password)
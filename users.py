from register import AdminRegister, Register, StudentRegister

class User:
    
    def __init__(self, username, password):
        super().__init__(username, password)

    


class Admin(User, AdminRegister):
    def __init__(self, username, password):
        super().__init__(username, password)
    

# admin = Admin("alireza", "alireza")
# print(admin.user)

class Student(User, StudentRegister):
    def __init__(self, username, password):
        super().__init__(username, password)


# admin = Admin("alireza", "18")
# admin.admin_validate()
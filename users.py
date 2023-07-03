from register import AdminRegister, Register, StudentRegister
from show import AdminShow, UserShow

class User:
    
    def __init__(self, username, password):
        super().__init__(username, password)

    


class Admin(User, AdminRegister, AdminShow):
    def __init__(self, username, password):
        super().__init__(username, password)
    

# admin = Admin("alireza", "alireza")
# print(admin.user)

class Student(User, StudentRegister, UserShow):
    def __init__(self, username, password):
        super().__init__(username, password)


# admin = Admin("alireza", "18")
# admin.admin_validate()
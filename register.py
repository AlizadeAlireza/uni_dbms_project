from helper_script import admin_username, admin_password

class Register:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AdminRegister(Register):
    def __init__(self, username, password):
        super().__init__(username, password)

    def admin_validate(self):
        if (self.username == admin_username and self.password == admin_password):
            return True

class StudentRegister(Register):
    def __init__(self, username, password):
        super().__init__(username, password)

    def student_validate(self):
        pass
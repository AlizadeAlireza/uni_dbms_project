from helper_script import admin_username, admin_password

class Register:
    
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def admin_validate(self):
        username = input(" please enter your userName: ")
        password = input(" please enter your pass: ")

        if (username == admin_username and password == admin_password):
            return True

    def student_validate(self):
        username = input(" please enter your userName: ")
        password = input(" please enter your pass: ")

        pass
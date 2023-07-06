"""
This script defines user classes for different roles (Admin and Student) and combines functionality from various inherited classes. It includes the following classes:

- User: The base class for user objects.
    - __init__(username, password): Initializes the User object with a username and password.

- Admin: Inherits from User class and combines functionality from AdminRegister, AdminShow, and AdminAbility classes.
    - __init__(username, password): Initializes the Admin object with a username and password.

- Student: Inherits from User class and combines functionality from StudentRegister, UserShow, and StudentAbility classes.
    - __init__(username, password): Initializes the Student object with a username and password.

Note: The script assumes the existence of classes from the abilities, register, and show modules. The abilities module provides abilities specific to user roles (Admin and Student), the register module provides registration functionality, and the show module provides methods for displaying information from a database.

To use the script, create instances of the Admin and Student classes by providing a username and password. These objects will have combined functionality from their respective inherited classes, allowing them to perform actions based on their role.


"""



from abilities import AdminAbility, StudentAbility
from register import AdminRegister, Register, StudentRegister
from show import AdminShow, UserShow

class User:
    # def __init__(self, username, password):
    #     super().__init__(username, password)
    pass

class Admin(User,  AdminRegister, AdminShow, AdminAbility):
    def __init__(self, username, password):
        super().__init__(username, password)
    

class Student(User,  StudentRegister, UserShow, StudentAbility):
    def __init__(self, username, password):
        super().__init__(username, password)

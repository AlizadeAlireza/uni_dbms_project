"""
This script includes classes for user registration and validation.

The script includes the following main components:

1. Import statements: It imports necessary variables and classes from other modules.

2. Register class: The `Register` class is the base class for user registration. It has attributes for username and password.

3. AdminRegister class: The `AdminRegister` class inherits from the `Register` class. It provides functionality to validate admin credentials. It compares the provided username and password with the values stored in the `admin_username` and `admin_password` variables from the `helper_script` module. If the credentials match, it returns `True`, indicating a successful validation.

4. StudentRegister class: The `StudentRegister` class also inherits from the `Register` class. It provides functionality to validate student credentials. It retrieves the student's information from the database by executing a query with the provided student ID (password) and verifies that the username matches the retrieved student name. If the validation is successful, it returns a tuple containing `True` and the student ID.

5. Helper script: The `helper_script` module contains the `admin_username` and `admin_password` variables, which store the admin's username and password, respectively.

The `AdminRegister` and `StudentRegister` classes take username and password as input parameters in their constructor and inherit the `username` and `password` attributes from the `Register` class.

The `admin_validate` method in the `AdminRegister` class validates the admin's credentials by comparing the provided username and password with the stored admin username and password.

The `student_validate` method in the `StudentRegister` class validates the student's credentials by retrieving the student's information from the database and comparing the provided username with the retrieved student name.

Note: The script assumes the existence of the `helper_script` module and the `Connection` class from the `connections` module. It also assumes the presence of a database connection and appropriate table structures for retrieving student information.

"""


from helper_script import admin_username, admin_password
from connections import Connection

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
        # getting user / pass
        # user : name
        # pass : id
        # get pass

        database_connection = Connection()

        try:
            query = f"SELECT * FROM STT WHERE STT.STID = {self.password}"
        except:
            return "no id"

        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, "")
        stt_row = cursor.fetchone()
        database_connection._close(cursor,connection)

        if (stt_row.STName.strip() == self.username.strip()):
            return (True, stt_row.STID)
# s = StudentRegister("ali", 1)

# a = s.student_validate()
# print(a)
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
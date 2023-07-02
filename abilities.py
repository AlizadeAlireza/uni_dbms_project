from helper_script import department_id
from connections import Connection
import pyodbc

class Abilitiy:
    # a = "for student"
    def available_courses(self):
        pass
    def show_informations(self):
        pass
    def select_course(self):
        pass
    def remove_course(self):
        pass
    def total_average(self):
        pass
    def term_average(self):
        pass

class AdminAbility(Abilitiy):
    id = 0
    def remove_default_course(self):
        pass
    def add_course(self):
        pass

    def add_student(self):
        database_connection = Connection()

        id = str(self.id)
        name = input(" name : ")
        major = input (" major ")
        level = input (" bs / phd / ms ") # hint : helper function
        de_id = department_id()
        query = "INSERT INTO STT (STID, STName, STMJR, STLev, STDEID) VALUES (?,?,?,?,?)"
        values = (id, name, major, level, de_id)

        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, values)
        database_connection._close(cursor,connection)

        self.id += 1   #error id is not correct !!
        
    def add_professor(self):
        pass

class StudentAbility(Abilitiy):
    pass

b = AdminAbility()
print(b.add_student())
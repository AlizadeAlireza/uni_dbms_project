from helper_script import department_id, lesson_type
from connections import Connection
import pyodbc

class Abilitiy:
    # a = "for student"
    def available_courses(self):
        pass
        # it is about fetching all the cources and print it
    def show_informations(self):
        pass
        # maybe i delete this
        # maybe can fetch the row and print the informations
    def select_course(self):
        pass
        # in the available courses
        # user can select the course and submit it in stcot table
    def remove_course(self):
        pass
        # user can delete the course that select ---> delete from STCOT
    def total_average(self):
        pass
        # it is a query and after execute we can return it
        # the query get all the grades for that student
    def term_average(self):
        pass
        # it is a query and after execute we can return it
        # the query get just the term grades for that student

class AdminAbility(Abilitiy):
    id = 0
    def remove_default_course(self):
        database_connection = Connection()

        # like add student
        # we pass the parameters in the query 
        # just like add students

         # hint : helper function
        lesson_id = int(input("\nenter lesson ID : "))
        delete_query = "DELETE FROM COT WHERE COID = ?"
        values = (lesson_id)

        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, delete_query, values)
        database_connection._close(cursor,connection)
        # can drop the row with first fetching and after delete that row
    def add_course(self):
        database_connection = Connection()

        # like add student
        # we pass the parameters in the query 
        # just like add students
        type = lesson_type()
        de_id = department_id()
        title = input(" title : ")
        credit = input (" credit ")
        
        query = "INSERT INTO COT (CODEID, CoTitle, Credit, COtype) VALUES (?,?,?,?)"
        values = (de_id, title, credit, type)

        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, values)
        database_connection._close(cursor,connection)

    def add_student(self):
        database_connection = Connection()

        # id = str(self.id)
        name = input(" name : ")
        major = input (" major ")
        level = input (" bs / phd / ms ") # hint : helper function
        de_id = department_id()
        query = "INSERT INTO STT (STName, STMJR, STLev, STDEID) VALUES (?,?,?,?)"
        values = (name, major, level, de_id)

        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, values)
        database_connection._close(cursor,connection)

        # self.id += 1   #error id is not correct !!
        
    def add_professor(self):
        pass
        # like add student we 
        # pass the elemnts and execute the query

class StudentAbility(Abilitiy):
    pass

b = AdminAbility()
print(b.remove_default_course())
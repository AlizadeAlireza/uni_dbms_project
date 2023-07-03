"""

show for admin and every fucking guy
"""
from connections import Connection
class Show:
    def available_courses(self):
        
        database_connection = Connection()
        query = f"SELECT * FROM COT"
        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, "")
        database_connection._fetch(cursor)
        database_connection._close(cursor,connection)
        # it is about fetching all the cources and print it

    def student_information(self):
        database_connection = Connection()
        value = int(input("\n enter the student ID: "))
        query = f"SELECT * FROM STT WHERE STT.STID = {value}"
        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, "")
        database_connection._fetch(cursor)
        database_connection._close(cursor,connection)

class AdminShow(Show):
    def show_tables(self):

        database_connection = Connection()
        value = input("\nenter your table name: ")
        query = f"SELECT * FROM {value}"
        cursor, connection = database_connection._open()
        database_connection._execute(cursor, connection, query, "")
        database_connection._fetch(cursor)
        database_connection._close(cursor,connection)
        

class UserShow(Show):
    pass


show = AdminShow()
show.available_courses
()
"""
This script provides classes for displaying information from a database. It includes the following classes:

- Show: The base class for displaying information.
    - available_courses(): Displays all available courses from the "COT" table.
    - student_information(): Displays information about a specific student based on their ID.

- AdminShow: Inherits from Show class and includes an additional method for displaying tables.
    - show_tables(): Displays all rows from a specified table based on user input.

- UserShow: Inherits from Show class. Currently does not have any additional methods.

Note: The script uses the Connection class from the connections module to establish a connection with the database and execute SQL queries.

To use the script, create an instance of the desired class and call the appropriate method to display the information.


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


# show = AdminShow()
# show.available_courses()
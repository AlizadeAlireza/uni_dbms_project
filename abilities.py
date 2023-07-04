from helper_script import department_id, lesson_type, student_level
from connections import Connection

class Abilitiy:
    def select_course(self, student_id):     #only admin can add the grade 
        database_connection = Connection()
        try:
            lesson_id = int(input("enter lesson ID: "))
            term = int(input("term : "))
            year = input(" year : ")
            grade = input (" grade:  ")
            
            query = "INSERT INTO STCOT (STID, COID, TR, YRYR, Grade) VALUES (?,?,?,?,?)"
            values = (student_id,lesson_id, term, year, grade)

            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, query, values)
            database_connection._close(cursor,connection)
            print("\nselect the course successfully!")
        except Exception as e:
            print("An error occurred while adding the course:")
            print(e)
        # in the available courses
        # user can select the course and submit it in stcot table
    def remove_course(self, student_id):
        database_connection = Connection()
        try:
            lesson_id = int(input("enter lesson ID: "))
            query = "DELETE from STCOT where STCOT.STID = ? AND STCOT.COID = ?"
            values = (student_id,lesson_id)

            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, query, values)
            database_connection._close(cursor,connection)

            print("\nremove the course successfully!!")
        except Exception as e:
            print("An error occurred while adding the course:")
            print(e)
        # user can delete the course that select ---> delete from STCOT
    
        
    def student_average(self, student_id):
        database_connection = Connection()
        try:
            query = f""" select STT.STNAME,STT.STID,
                sum(STCOT.Grade*COT.CREDIT)/sum(COT.CREDIT) as AVE from
                STT,COT,STCOT
                where STT.STID = STCOT.STID  and COT.COID = STCOT.COID and STT.STID = {student_id}
                group by STT.STNAME,STT.STID """


            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, query, "")
            database_connection._fetch(cursor)
            database_connection._close(cursor,connection)
        except Exception as e:
            print("An error occurred while calculating the student average!")
            print(e)

class AdminAbility(Abilitiy):
    def remove_default_course(self):
        database_connection = Connection()

        # hint : helper function
        try:
            lesson_id = int(input("\nenter lesson ID : "))
            delete_query = "DELETE FROM COT WHERE COID = ?"
            values = (lesson_id)

            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, delete_query, values)
            database_connection._close(cursor,connection)
            # can drop the row with first fetching and after delete that row

            print("\n remove the default course by admin successfully!")
        except Exception as e:
            print("An error occurred while adding the course:")
            print(e)
    def add_course(self):
        database_connection = Connection()

        try:
            type = lesson_type()
            de_id = department_id()
            title = input("title : ")
            credit = input ("credit:  ")
            
            query = "INSERT INTO COT (CODEID, CoTitle, Credit, COtype) VALUES (?,?,?,?)"
            values = (de_id, title, credit, type)

            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, query, values)
            database_connection._close(cursor,connection)
            
            print("\nCourse added successfully!")

        except Exception as e:
            print("An error occurred while adding the course!")
            print(e)


    def add_student(self):
        database_connection = Connection()

        try:
            name = input("name : ")
            major = input("major: ")
            level = student_level() # hint : helper function
            de_id = department_id()
            query = "INSERT INTO STT (STName, STMJR, STLev, STDEID) VALUES (?,?,?,?)"
            values = (name, major, level, de_id)

            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, query, values)
            database_connection._close(cursor,connection)

            print("\nStudent added successfully!")

        except Exception as e:
            print("An error occurred while adding the student!")
            print(e)
        
    def add_professor(self):
        pass
        # like add student we 
        # pass the elemnts and execute the query

    def total_average(self):
        database_connection = Connection()
        try:
            query = f""" select STT.STNAME,STT.STID,
            sum(STCOT.Grade*COT.CREDIT)/sum(COT.CREDIT) as AVE from
            STT,COT,STCOT
            where STT.STID = STCOT.STID  and COT.COID = STCOT.COID
            group by STT.STNAME,STT.STID """


            cursor, connection = database_connection._open()
            database_connection._execute(cursor, connection, query, "")
            database_connection._fetch(cursor)
            database_connection._close(cursor,connection)
        except Exception as e:
            print("An error occurred while calculating the average.")
            print(e)
    # def remove_student(self, student_id):
    #     database_connection = Connection()

    #      # hint : helper function
    #     delete_query = "DELETE FROM STT WHERE STT.STID = ?"
    #     values = (student_id)
    #     cursor, connection = database_connection._open()
    #     database_connection._execute(cursor, connection, delete_query, values)
    #     database_connection._close(cursor,connection)
    

class StudentAbility(Abilitiy):
    pass

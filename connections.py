# this is the first commit for upload and create this repository

# imports
import pyodbc


# Connection
class Connection:
    def connection_test(self):
        # connection details
        server = "MSI"
        database = "uni__project"
        # username = "MSI\pc"
        # password = ""

        # create connection with f String --> f""
        connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes"
        # stablish connection
        # to ensure is connected!!
        try: 
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            # Execute a test query
            cursor.execute("SELECT 1")
            # Fetch the result
            result = cursor.fetchone()
            # Check if the result is as expected
            if result[0] == 1:
                print("Connection successful!")
            else:
                print("Connection failed!")

            # Close the cursor and connection
            cursor.close()
            connection.close()

        except pyodbc.Error as e:
            print("Connection failed!")
            print(f"Error message: {str(e)}")

    def _open(self):
        server = "MSI"
        database = "uni__project"
        connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes"
        
        try: 
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            return cursor, connection
        except pyodbc.Error as e:
            print("Connection failed!")
            print(f"Error message: {str(e)}")
    
    def _close(self,cursor, connection):
        cursor.close()
        connection.close()

   
    def _execute(self, cursor, connection, query, values):

        if values != "":
            cursor.execute(query, values)       
            connection.commit()
        else:  
            cursor.execute(query)
    
    def _fetch(self, cursor):

        rows = cursor.fetchall()
        for row in rows:
            print(row)


# call the connection
# connection = Connection()
# # call
# # print(type(connection))
# connection.connection_test()
"""
This script defines a `Connection` class for establishing and managing a database connection using the `pyodbc` module.

The script includes the following main components:

1. Import statement: It imports the `pyodbc` module for working with ODBC connections.

2. Connection class: The `Connection` class provides methods for managing the database connection. It has the following methods:
   - `connection_test`: This method tests the connection by attempting to execute a test query. It prints a success message if the connection is established and the test query returns the expected result.
   - `_open`: This private method opens the database connection by creating a connection string and using it to establish a connection. It returns a cursor object and the connection object.
   - `_close`: This private method closes the database connection by closing the cursor and the connection.
   - `_execute`: This private method executes a query with optional parameter values. It takes a cursor, connection, query string, and values as input. If values are provided, it executes the query with the values and commits the changes to the database. If no values are provided, it executes the query without any parameterization.
   - `_fetch`: This private method fetches the results of a query from the cursor and prints them.

The `Connection` class provides a convenient way to establish a database connection, execute queries, and handle query results. It assumes the presence of a SQL Server and a database named `uni__project` on the local machine, and it uses Windows Authentication for connecting to the server.

To use the `Connection` class, create an instance of the class and call the appropriate methods based on your requirements.

Note: The script assumes that the `pyodbc` module is installed and available for import.

"""

import pyodbc

# Connection
class Connection:
    def connection_test(self):
        # connection details
        server = "MSI"
        database = "uni__project"

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
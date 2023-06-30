# this is the first commit for upload and create this repository

# imports
import pyodbc



# connection function 
def connection_to_db ():
    # connection details
    server = "MSI"
    database = "uni_project"
    username = "MSI\pc"
    password = ""

    # create connection with f String --> f""
    connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes"









# stablish connection
# to ensure is connected!!


# try: 
#     connection = pyodbc.connect(connection_string)
#     cursor = connection.cursor()

#     # Execute a test query
#     cursor.execute("SELECT 1")

#     # Fetch the result
#     result = cursor.fetchone()

#     # Check if the result is as expected
#     if result[0] == 1:
#         print("Connection successful!")
#     else:
#         print("Connection failed!")

#     # Close the cursor and connection
#     cursor.close()
#     connection.close()

# except pyodbc.Error as e:
#     print("Connection failed!")
#     print(f"Error message: {str(e)}")
"""

    this script is for our tables and work with these

"""
import pyodbc


def create_table():
    pass


def create_tables():
    # Connection details
    server = "MSI"
    database = "uni__project"

    # Create connection string
    connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes"

    # Establish a connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # SQL queries to create tables
    create_table_queries = [
    """
    CREATE TABLE STT (
        STID CHAR(20) NOT NULL PRIMARY KEY,
        STName CHAR(100),
        STMJR CHAR(20),
        STLev CHAR(20),
        STDEID CHAR(20)
    )
    """,
    """
   CREATE TABLE COT (
        COID CHAR(20) NOT NULL PRIMARY KEY,
		CODEID CHAR(20),
        COTitle VARCHAR(100),
        Credit INT,
        COtype CHAR(20)
    )
    """,
    """
    CREATE TABLE STCOT (
        STID CHAR(20),
        COID CHAR(20),
        TR INT,
        YRYR INT,
        Grade FLOAT,
        PRIMARY KEY (STID, COID, TR, YRYR),
        FOREIGN KEY (STID) REFERENCES STT(STID),
        FOREIGN KEY (COID) REFERENCES COT(COID)
    )
    """,
    """
    CREATE TABLE PREREQ (
        COID CHAR(20),
        PRECOID CHAR(20),
		PRIMARY KEY (COID, PRECOID),
        FOREIGN KEY (COID) REFERENCES COT(COID)
    )
    """,
    """
    CREATE TABLE DEPT(
	DEID CHAR(20) NOT NULL PRIMARY KEY,
	MGRID CHAR(20),
    DEtitle varchar(100),
    phone char(12),
    address varchar(200),
    )
    """
      ,
    """
    CREATE TABLE PROF (
        PRID CHAR(20) NOT NULL PRIMARY KEY,
        PRname VARCHAR(100),
        RANKK CHAR(20),
        DEID CHAR(20),
        FOREIGN KEY (DEID) REFERENCES DEPT(DEID)
    )
    """,
    """
    CREATE TABLE PRCO (
        PRID CHAR(20),
        COID CHAR(20),
        GROUP_ID CHAR(10),
        PRIMARY KEY (PRID, COID, GROUP_ID),
        FOREIGN KEY (PRID) REFERENCES PROF(PRID),
        FOREIGN KEY (COID) REFERENCES COT(COID)
    )
    """
    
]

    try:
        # Execute the queries to create the tables
        for query in create_table_queries:
            cursor.execute(query)
        connection.commit()
        print("Tables created successfully!")
    except pyodbc.Error as e:
        print(f"Error creating tables: {str(e)}")

    # Close the cursor and connection
    cursor.close()
    connection.close()
    # end of function

# Call the function to create the tables
create_tables()




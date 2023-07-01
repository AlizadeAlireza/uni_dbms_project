"""

    this script is for our tables and work with these

"""
import pyodbc


def create_table():
    pass


def create_tables():
    # Connection details
    server = "MSI"
    database = "uni_project"

    # Create connection string
    connection_string = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes"

    # Establish a connection
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # SQL queries to create tables
    create_table_queries = [
    """
    CREATE TABLE STT (
        STID CHAR(10) NOT NULL PRIMARY KEY,
        STName VARCHAR(100),
        STNJR CHAR(20),
        STDEID CHAR(20)
    )
    """,
    """
    CREATE TABLE COT (
        COID CHAR(10) NOT NULL PRIMARY KEY,
        COTitle VARCHAR(100),
        Credit INT,
        COtype CHAR(20)
    )
    """,
    """
    CREATE TABLE STCOT (
        STID CHAR(10),
        COID CHAR(10),
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
        COID CHAR(10),
        PRECOID CHAR(10) PRIMARY KEY,
        FOREIGN KEY (COID) REFERENCES COT(COID)
    )
    """,
    """
    CREATE TABLE DEPT (
        MGRID CHAR(10),
        DEID CHAR(10) NOT NULL PRIMARY KEY,
        DEtitle VARCHAR(100),
        phone CHAR(12),
        address VARCHAR(200),
        FOREIGN KEY (MGRID) REFERENCES PROF(PRID)
    )
    """,
    """
    CREATE TABLE PROF (
        PRID CHAR(10) NOT NULL PRIMARY KEY,
        PRname VARCHAR(100),
        RANKK CHAR(20),
        DEID CHAR(10),
        FOREIGN KEY (DEID) REFERENCES DEPT(DEID)
    )
    """,
    """
    CREATE TABLE PRCO (
        PRID CHAR(10),
        COID CHAR(10),
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

# Call the function to create the tables
create_tables()




"""
CREATE DATABASE uni;

CREATE TABLE STT (
	STID CHAR(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    STName VARCHAR(100),
    STNJR char(20),
    STDEID char(20)
);

CREATE TABLE COT (
	COID CHAR(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    COTitle VARCHAR(100),
    Credit INT,
    COtype CHAR(20)
);

CREATE TABLE STCOT (
	STID CHAR(10),
    COID CHAR(10),
    TR INT PRIMARY KEY,
    YRYR INT PRIMARY KEY,
    Grade Float,
    foreign key(STID) references STT(STID),
    foreign key(COID) references COT(COID)
);

CREATE TABLE PREREQ(
	COID CHAR(10),
    PRECOID CHAR(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    foreign key(COID) references COT(COID)
);

CREATE TABLE DEPT(
	MGRID CHAR(10),
	DEID CHAR(10)  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DEtitle varchar(100),
    phone char(12),
    address varchar(200),
    foreign key(MGRID) references PROF(PRID)
    
);

CREATE TABLE PROF(
	PRID char(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PRname varchar(100),
    RANKK char(20),
	DEID CHAR(10),
    foreign key (DEID) references DEPT(DEID)
);

CREATE TABLE PRCO(
	PRID char(10) PRIMARY KEY,
    COID char(10) PRIMARY KEY,
    GROUP_ID char(10) PRIMARY KEY,
    foreign key (PRID) references PROF(PRID),
    foreign key (COID) references COT(COID)
);

"""
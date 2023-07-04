# University Project

This repository contains a Python-based university project management system. It provides functionalities for registering administrators and students, managing courses, and performing various operations related to student enrollment, course selection, and grading.

## Features

- **Admin Panel**: Allows administrators to manage courses, add and remove students, view student information, calculate average grades, and perform other administrative tasks.
- **User Panel**: Allows students to view available courses, select and remove courses, view their own information, calculate their average grades, and perform other user-specific operations.
- **Help/About**: Provides information about the system and its functionalities, as well as guidance on how to use the system effectively.
- **Database Connection**: Utilizes the `pyodbc` module to establish a connection with a SQL Server database for storing and retrieving data.

## Prerequisites

- Python 3.7 or above
- `pyodbc` module
- SQL Server with a database named `uni__project`
- Windows operating system (for Windows Authentication with SQL Server)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/AlizadeAlireza/uni_dbms_project.git

2. Install the required dependencies. In the project directory, run:
    ```shell
    pip install pyodbc

3. Set up the SQL Server connection:

Ensure that you have SQL Server installed and running.
Create a database named uni__project.
Modify the connection details in the connections.py script to match your SQL Server configuration.

    ```shell
    python main.py



## Usage

1. Upon running the application, you will be presented with a main menu.

2. Choose the desired option:

    - Register: Allows you to sign in as an administrator or student.

    - Help/About: Provides information and assistance on using the system.

    - Exit: Terminates the application.

3. Follow the prompts and navigate through the different menus to perform the desired operations.

Contributing

Contributions to the university project system are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.



Objects : 

1, connection  

    we can say first check the connection test.
    if we had an error we can handle it and work with the new mistakes.
    
    but if we have a true connection, we can continue.

2,  tables

    for this i have a new idea.
    if we have a tables class we can define some functions like add, delete, edit and ...

    a user can inherit this options and super user or regular user can use it.

    so create tables can be just a part of this sections.

3, user class :
    1. regular user
    2. super user 

` i think reg user can use UserClass and super user can have more abilities.`

4, menu

    1, search
    2, add
    3, edit
    4, remove
    5, exit


    add: 
        - getting values
        - if value exicts
        - error handling
    
    edit: 
        - getting value
        - !addValue
        - error handling

    remove: 
        - getting value
        - !addValue
        - error handling

## menu

## user terminal interface

### abstract
    1. option choosing :
        can select an option

    2. back to main menu: 
        can back to recent menu

## options

###  menus
0. welcome masseage :

    is a text in main menu




1. Register : 

    for this if we are user, our options can be different with admin panel.

    like add and edit for admin.
    but user can't see this things.

    validation ---> if exict ----> enter 
    if not exict ----> "text : invalid"  ///// error handle

    1. name
    2. last name
    3. phone_number
    4. student_id
    5. year
    6. back to main menu

        1. student panel :

            1. show the COT table ---> for see the courses:
                - back to student panel
            2. show the student information:
                - back to student panel
            3. student STCOT for every course std has:
                - back to student panel
            4. average : getting arument
                - calculate 
                - by terms
                - by all 
                - back to student panel
            
            5. getting courses: adding to STCOT ---> condition : 

            6. back to main menu

        4. admin panel : ----> create table and fetch to get the validation
            1. admin information
            2. add course 
            3. add professor
            4. add student 
            5. show : student informations, professor information, STCOT
            6. if average() ---> student number
            7. back to main menu

2. help/about :

    a script that have text

    can have a menu
    
    1. help 
    2. about
    3. back to main menu

set the invalid choices.

5. exit
    


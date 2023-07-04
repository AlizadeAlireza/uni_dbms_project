"""
This script provides functions and variables related to user input and helper functions for a student project.

The script includes the following functions:

1. department_id(): Prompts the user to select a department and returns the corresponding department ID based on the input.

2. lesson_type(): Prompts the user to select a lesson type and returns the corresponding type (amali/nazari) based on the input.

3. help(): Returns a string containing a test message for the help function.

4. about(): Returns a string containing a test message for the about function.

5. student_level(): Prompts the user to select a student level and returns the corresponding level (bs/phd/ms) based on the input.

The script also includes the following variables:

1. admin_username: Represents the username for an admin user.
2. admin_password: Represents the password for an admin user.

These functions and variables can be used as part of the student project's functionality.

Note: The script does not provide a complete implementation of the project's logic. It only includes the user input functions and test helper functions.

"""


admin_username = "admin"
admin_password = "admin"

def department_id():
    department = input("1, fanni /2, ensani/3, tarbiat: " )
    try:
        if department == "1":
            stdeid = "1"
        elif department == "2":
            stdeid = "2"
        elif department == "3":
            stdeid = "3"
        return stdeid
    except:
        print("\nthere is no such DEPARTMENT!")
    
def lesson_type():
    type = input("\n1, amali /2, nazari: " )
    try:
        if type == "1":
            lesson_type = "amali"
        elif type == "2":
            lesson_type = "nazari"
        else:
            print("\nthere is no such lesson type!")

        return lesson_type
        
    except:
        print("\nthere is no such lesson type!")

def help():
    a = "\nthis is a test for our help function to show that." 
    return a

def about():
    a = "\nthis is a test for our about function to show that."
    return a


def student_level():
    level = input(" \nselect the level: 1, bs / 2, phd / 3, ms: ")
    try:
        if level == "1":
            stu_level = "bs"
        elif level == "2":
            stu_level = "phd"
        elif level == "3":
            stu_level = "ms"
        return stu_level
    except:
        return "there is no such DEPARTMENT!"

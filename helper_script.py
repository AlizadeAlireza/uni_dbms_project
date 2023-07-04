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
    help_text = """\nUniversity Project Management System Help
    
    Welcome to the University Project Management System! This system provides functionalities for administrators and students to manage courses, enrollment, and grading. Below is a list of available commands and their descriptions:
    
    1. help: Display this help message.
    2. about: Display information about the project.
    3. exit: Exit the program.
    
    Admin Commands:
    4. available_courses: Display the list of available courses.
    5. add_course: Add a new course to the system.
    6. remove_default_course: Remove a default course from the system.
    7. student_information: View information about a specific student.
    8. select_course: Select a course for a student.
    9. remove_course: Remove a course from a student's selection.
    10. remove_student: Remove a student from the system.
    11. add_student: Add a new student to the system.
    12. total_average: Calculate the total average grade of all students.
    13. student_average: Calculate the average grade of a specific student.
    
    User Commands:
    14. available_courses: Display the list of available courses.
    15. student_information: View your information.
    16. select_course: Select a course from the available courses.
    17. remove_course: Remove a course from your selection.
    18. student_average: Calculate your average grade.
    
    Note: Please enter the corresponding command number to execute the desired operation."""
    return a

def about():
    about_text = """
        \nUniversity Project Management System - About
        
        The University Project Management System is a Python-based application developed for managing university courses, student enrollment, and grading. It provides separate functionalities for administrators and students to perform their respective tasks.
        
        This project is developed as part of a university project and is intended for educational purposes. It demonstrates the use of object-oriented programming principles, SQL database integration, and command-line user interfaces.
        
        For any inquiries or feedback, please contact the project developers.
    """
    return about_text


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

"""
This script implements the main logic for a student project.

The script includes the following main components:

1. Import statements: It imports necessary modules and classes for the project.

2. Main function: The main entry point of the script. It contains a loop that displays the main menu and handles user choices.

3. Menu class: The Menu class provides methods to display different menus, such as the main menu, register menu, admin register menu, user register menu, and help/about menu.

4. Register classes: The Register, AdminRegister, and StudentRegister classes handle user registration functionalities.

5. Tables module: The create_tables function is used to create necessary database tables for the project.

6. Ability classes: The Abilitiy, AdminAbility, and StudentAbility classes define various abilities that users can perform, such as selecting courses, removing courses, calculating averages, adding students, and more.

7. User classes: The Admin and Student classes represent the admin and student users, respectively. They include methods for validating user credentials and accessing specific functionalities.

8. Helper script: The helper_script module includes helper functions for handling department IDs, lesson types, and student levels.

The main function sets up an infinite loop that displays the main menu and prompts the user for choices. Based on the user's choice, the script performs various actions, such as user registration, accessing different menus, performing admin or student-related functionalities, and displaying help/about information.

Note: The script assumes the existence of other modules, classes, and functions required for the project. Some of the implementation details and missing parts are not included in the script. This docstring provides an overview of the script's main components and functionalities.

"""


# imports
import msvcrt
from menu import Menu
from register import Register, AdminRegister, StudentRegister
from tables import create_tables
from abilities import Abilitiy, AdminAbility, StudentAbility
from users import Admin, Student
from helper_script import help, about

def main():

    # create instance of classes
    menu = Menu()

    # create a loop for menu
    while True:
        # call the main menu
        menu.main_menu()

        # get the choice
        choice = int(input("\nplease enter your option: "))

        # choosing system
        if choice == 1: # REGISTER
            print("\ngoing to register menu...")
            while True:
                menu.register_menu()
                choice = int(input("\nplease enter your position: "))
                if choice == 1:
                    print("\n*** SIGN IN ***\n")
                    # get the pass and name
                    username = input(" please enter your userName: ")
                    password = input(" please enter your pass: ")
                    # admin instance
                    admin = Admin(username, password)
                    valid_admin = admin.admin_validate()
                    if valid_admin == True:
                        print("\ngoing to admin panel..")
                        menu.admin_register_menu()
                    else: 
                        print("\nwrong info for admin register")
                        break
                    while True:
                        choice = int(input("\nplease enter your option: "))
                        if choice == 1:
                            admin.available_courses()
                            menu.admin_register_menu()
                        elif choice == 2:
                            admin.add_course()
                            menu.admin_register_menu()
                        elif choice == 3:
                            admin.remove_default_course()
                            menu.admin_register_menu()
                        elif choice == 4:
                            admin.student_information()
                            menu.admin_register_menu()
                        elif choice == 5:
                            student_id = int(input("\nenter student id: "))
                            admin.select_course(student_id)
                            menu.admin_register_menu()
                        elif choice == 6:
                            student_id = int(input("\nenter student id: "))
                            admin.remove_course(student_id)
                            menu.admin_register_menu()
                        elif choice == 7:
                            student_id = int(input("\nenter student id: "))
                            admin.remove_student(student_id)
                            menu.admin_register_menu()
                        elif choice == 8:
                            admin.add_student()
                            menu.admin_register_menu()
                        elif choice == 9:
                            admin.total_average()
                            menu.admin_register_menu()
                        elif choice == 10:
                            student_id = int(input("\nenter student id: "))
                            admin.student_average(student_id)
                            menu.admin_register_menu()
                        elif choice == 11:
                            print("\nback to register menu...")
                            break
                elif choice == 2:
                    print("\n*** SIGN IN USER ***\n")
                    # get the pass and name
                    username = input(" please enter your userName: ")
                    password = input(" please enter your pass: ")

                    user = Student(username, password)
                    valid_user, user_id = user.student_validate()
                    if valid_user == True:
                        print("\ngoing to user panel..")
                        menu.user_register_menu()
                    while True:
                        choice = int(input("\nplease enter your option: "))
                        if choice == 1:
                            user.available_courses()
                            menu.user_register_menu()
                        elif choice == 2:
                            user.student_information()
                            menu.user_register_menu()
                        elif choice == 3:
                            user.select_course(user_id)
                            menu.user_register_menu()
                        elif choice == 4:
                            user.remove_course(user_id)
                            menu.user_register_menu()
                        elif choice == 5:
                            user.student_average(user_id)
                            menu.user_register_menu()
                        elif choice == 6:
                            print("\nback to register menu...")
                            break
                elif choice == 3:
                    # back to main menu
                    print("\nback to main menu...")
                    break
                
        elif choice == 2: # HELP/ABOUT
            print("\n going to help/about page... ")
            menu.help_about_menu()
            while True:
                choice = int(input("\nplease enter your option: "))
                if choice == 1:
                    print(help())
                    print("\npress any key to help/about menu...", end = "", flush = True)
                    msvcrt.getch()
                    menu.help_about_menu()
                    # press any key to going to help/about page
                    # hint : i can use a function
                elif choice == 2:
                    print(about())
                    print("\npress any key to help/about menu...", end = "", flush = True)
                    msvcrt.getch()
                    menu.help_about_menu()
                elif choice == 3:
                    print("\nback to main menu...")
                    break

        elif choice == 3:
            print("\n*** good luck ***")
            break    
        else:
            print("\n*** wrong choice ***")
            menu.main_menu()

main()
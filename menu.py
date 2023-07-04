"""
This script defines a Menu class that represents the different parts of a student project's terminal user interface.

The Menu class provides various methods to display different menus and options to the user. Here's an overview of the available menus:

1. main_menu(): Displays the main menu options, including registration, help/about, and program exit.

2. register_menu(): Displays the register menu options, allowing the user to choose between admin and user registration or go back to the main menu.

3. user_register_menu(): Displays the options available in the student panel, such as viewing available courses, showing information, selecting/removing courses, calculating average, or going back to the register menu.

4. admin_register_menu(): Displays the options available in the admin panel, such as viewing available courses, adding/removing courses, showing student information, managing student courses, adding/removing students, calculating averages, or going back to the register menu.

5. help_about_menu(): Displays the options available in the help/about menu, including accessing help, information about the program, or going back to the main menu.

To use the Menu class, create an instance of the class and call the appropriate method to display the desired menu.

Note: The script does not handle user input or implement the functionality for each menu option. It only provides the menu display functionality.

"""


class Menu:
    ## main menu
    def main_menu(self):
        
        # welcome masseage
        print("\n*** student project ***\n\n  please choose an option (-_-)\n\n***main menu***\n")
        # Register
        print("1, Register")
        # help about
        print("2, help/about")
        # exit of the program
        print("3, exit of the program")

    ## Register menus

    # main register menu
    def register_menu(self):
        print("\n *** register menu ***\n")
        print("1. admin")
        print("2. user") # this name can be student
        print("3. back to main menu")
    
    # user register menu
    def user_register_menu(self):
        print("\n *** student panel ***\n")
        print("1. see the available courses")
        print("2. show the informations")
        print("3. select the course")
        print("4. remove the course (only in term)")
        print("5. average ")
        print("6. back to register menu")    
    # admin register menu
    def admin_register_menu(self):
        print("\n *** admin panel ***\n")
        print("1. see the available courses")
        print("2. add course")
        print("3. remove the course")
        print("4. show the student information") # can have another options
        print("5. select the course for student")
        print("6. remove the course from student program")
        print("7. remove the student ")
        print("8. add student")
        print("9. getting all students average")
        print("10. getting student average")
        print("11. back to register menu")    

    def help_about_menu(self):
        print("\n *** help/about menu ***\n")
        print("1. help")
        print("2. about")
        print("3. back to main menu")

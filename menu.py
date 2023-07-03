'''
    in this script we want to create a menu class and use it in our logics.
    the different parts of our std_project for terminal user interface.

'''

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

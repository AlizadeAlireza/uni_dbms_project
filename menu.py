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
        # print("5. edit the choosen courses")
        print("6. getting average by all terms")
        print("7. getting average by current term")
        print("8. back to register menu")    
    # admin register menu
    def admin_register_menu(self):
        print("\n *** admin panel ***\n")
        print("1. see the available courses")
        print(". add course")
        print(". remove the course")
        print(". show the student information") # can have another options
        print(". select the course for student")
        print(". remove the course from student program")
        print(". remove the student ")
        print(". add student")
        print(". getting student average by all terms")
        print(". getting student average by current term")
        print("11. back to register menu")    



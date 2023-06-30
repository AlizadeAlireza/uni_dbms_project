'''
    in this script we want to create a menu class and use it in our logics.
    the different parts of our std_project for terminal user interface.

'''

from atexit import register


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
        print("")
        print("")
        print(". back to register menu")    
    # admin register menu
    def admin_register_menu(self):
        print("\n *** admin panel ***\n")
        print("")
        print("")
        print(". back to register menu")    


# create instance of class
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
        menu.register_menu()
        while True:
            choice = int(input("\nplease enter your position: "))
            if choice == 1:
                menu.admin_register_menu()
            elif choice == 2:
                menu.user_register_menu()
            elif choice == 3:
                # back to main menu
                print("\ngoing to main menu...")
                break
            
    elif choice == 2:
        print("test -> you choose help/about  ")
    elif choice == 3:
        print("\n*** good luck ***")
        break
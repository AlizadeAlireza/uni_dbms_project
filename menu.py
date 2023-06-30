'''
    in this script we want to create a menu class and use it in our logics.
    the different parts of our std_project for terminal user interface.

'''

class Menu:
    # main menu
    def main_menu(self):
        
        # welcome masseage
        print("\n*** student project ***\n\n  please choose an option (-_-)\n")
        # Register
        print("1, Register")
        # help about
        print("2, help/about")
        # exit of the program
        print("3, exit of the program")

menu = Menu()
main_menu = menu.main_menu()
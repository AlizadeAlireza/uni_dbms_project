# imports

from menu import Menu
from register import Register
from tables import create_table

def main():

    # create instance of classes
    menu = Menu()
    register = Register()

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
                    valid_admin = register.admin_validate()
                    if valid_admin == True:
                        print("\ngoing to admin panel..")
                        menu.admin_register_menu()
                    # hint : re-enter, back to menu, (select enter password)
                    
                    while True:
                        choice = int(input("\nplease enter your option: "))
                        if choice == 11:
                            print("\nback to register menu...")
                            break
                elif choice == 2:
                    print("\ngoing to user panel..")
                    menu.user_register_menu()
                    while True:
                        choice = int(input("\nplease enter your option: "))
                        if choice == 8:
                            print("\nback to register menu...")
                            break
                elif choice == 3:
                    # back to main menu
                    print("\nback to main menu...")
                    break
                
        elif choice == 2: # HELP/ABOUT
            print("test -> you choose help/about  ")
        elif choice == 3:
            print("\n*** good luck ***")
            break    

main()
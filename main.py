# imports
import msvcrt
from menu import Menu
from register import Register, AdminRegister, StudentRegister
from tables import create_table
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
                    # hint : re-enter, back to menu, (select enter password)
                    
                    while True:
                        choice = int(input("\nplease enter your option: "))
                        if choice == 11:
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
                            pass
                        elif choice == 2:
                            pass
                        elif choice == 3:
                            pass
                        elif choice == 4:
                            pass
                        elif choice == 5:
                            pass
                        elif choice == 6:
                            pass
                        elif choice == 7:
                            pass
                        elif choice == 8:
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

main()
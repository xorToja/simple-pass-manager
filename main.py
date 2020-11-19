from colorama import init
from colorama import Fore, Back, Style
from menu import menu_one, menu_two, menu_three, menu_four

def show_menu():
    '''Display menu on terminal'''

    print('='*30)
    print('=' + ' '*12 + 'menu' + ' '*12 + '=')
    print('='*30)
    print('1. Add new record')
    print('2. Show All Apps/WebPages connected with Login/Email')
    print('3. Show Login and Password for App/WebPage')
    print('4. Generate New Password')
    print('5. Exit')
    print()
    menu_respond()

def menu_respond():
    '''Listener for user response'''

    while True:
        try:
            response = int(input(Fore.CYAN + 'Choose menu option: ' + Style.RESET_ALL))
            if response == 1:
                menu_one()
                show_menu()
            elif response == 2:
                menu_two()
                show_menu()
            elif response == 3:
                menu_three()
                show_menu()
            elif response == 4:
                menu_four()
                show_menu()
            elif response == 5:
                print(Fore.GREEN + 'Exiting...' + Style.RESET_ALL)
                exit()
                break
            else:
                print(Fore.RED + 'Number must be one of available menu options!')
        except ValueError:
            print(Fore.RED + 'Expected integer value, not char!' + Style.RESET_ALL)


if __name__ == '__main__':
    init()
    show_menu()

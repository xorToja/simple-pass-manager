from colorama import init
from colorama import Fore, Back, Style
from database_manager import show_connected_with_login, show_auth_data_for_app, add_new_row
from getpass import getpass
import random
import string
import os


def menu_one():
    '''Add new record'''
    while True:
        try:
            site = input(Fore.CYAN + 'Please, type in address to site or its name: ' + Style.RESET_ALL)
            login = input(Fore.CYAN + 'Please, type in login: ' + Style.RESET_ALL)
            while True:
                password = getpass(Fore.CYAN + 'Please, type in password: ' + Style.RESET_ALL)
                password2 = getpass(Fore.CYAN + 'Please, retype in password: ' + Style.RESET_ALL)
                if password == password2:
                    break
                else:
                    print(Fore.RED + 'Password are not matching, try again...' + Style.RESET_ALL)
                    continue
            description = input(Fore.CYAN + 'Optionaly add description: ' + Style.RESET_ALL)
            add_new_row(site, login, password, description)
            answer = input(Fore.CYAN + 'Do you want to add another record? 1 - Yes, 0 - No: ')
            if int(answer):
                print(Fore.GREEN + 'Adding another record' + Style.RESET_ALL)
                continue
            else:
                print(Fore.GREEN + 'Returning to menu' + Style.RESET_ALL)
                break

        except Exception as error:
            print(Fore.RED + 'Unexpected occurred while adding new record: ' + Style.RESET_ALL)
            print(error)
            break
        except ValueError:
            print(Fore.RED + 'Wrong value type! Try again...' + Style.RESET_ALL)
            break

def menu_two():
    '''Show All Apps/WebPages connected with Login/Email'''

    try:
        login = input(Fore.CYAN + 'Inpur login or email, to show connected records: ' + Style.RESET_ALL)
        show_connected_with_login(login)
    except Exception as error:
        print(Fore.RED + 'Unexpected error occurrs' + Style.RESET_ALL)
        print(error)

def menu_three():
    '''Show Login and Password for App/WebPage'''

    try:
        app = input(Fore.CYAN + 'Input web/app name, to show auth data: ' + Style.RESET_ALL)
        show_auth_data_for_app(app)
    except Exception as error:
        print(Fore.RED + 'Unexpected error occurrs' + Style.RESET_ALL)
        print(error)


def menu_four():
    '''Generate New Password'''

    digits = string.digits
    letters = string.ascii_letters
    punctuation = '!@#$%^&*?'

    print(Fore.MAGENTA + "If you want to go back to menu, type 0 (zero)..." + Style.RESET_ALL)
    while True:
        try:

            pass_len = int(input(Fore.CYAN + "How long should your password be? (between 6 and 20): " + Style.RESET_ALL))
            if pass_len == 0:
                print(Fore.CYAN + "Returning to menu..."  + Style.RESET_ALL)
                show_menu()
                break
            elif 6 <= pass_len <= 20:
                n_chars = round(pass_len*0.2)
                n_digits = round(pass_len*0.3)
                n_letters = round(pass_len*0.5)
                tmp_lett = "".join(random.choice(letters) for i in range(n_letters))
                tmp_dig = "".join(random.choice(digits) for i in range(n_digits))
                tmp_char = "".join(random.choice(punctuation) for i in range(n_chars))

                tmp_list = list(tmp_lett + tmp_dig + tmp_char)
                random.shuffle(tmp_list)
                password = "".join(tmp_list)

                print()
                print(Fore.GREEN + f'New password: {password} has been coppied to clipboard' + Style.RESET_ALL)
                print()
                os.system('echo ' + password.strip() + '| clip')
                break
            else:
                print(Fore.RED + 'Number must be between 6 and 20 (included)!' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Expected integer value, not char!' + Style.RESET_ALL)

from colorama import init
from colorama import Fore, Back, Style
from prettytable import PrettyTable
import sqlite3
import os

path = '.\manager_database.db'

def create_connection():
    '''creating connection to database \manager_database.db
        if database doesn't exist then create it'''

    global path
    try:
        if os.path.isfile(path):
            connection = sqlite3.connect(path)
            return connection
        else:
            create_database()
            print(f'database {path} created...')
            connection = sqlite3.connect(path)
            return connection

    except sqlite3.Error as error:
        print(Fore.RED + "an error occurr: " + error + Style.RESET_ALL)

def create_database():
    '''creating database with one table named users_table
        columns names: domain, login, password, description'''

    global path
    try:
        with sqlite3.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                            CREATE TABLE users_table
                            (domain text,
                             login text,
                             password text,
                             description text)
                            ''')
            connection.commit()
    except sqlite3.DatabaseError as error:
        print(Fore.RED + "database error: " + error + Style.RESET_ALL)

def show_connected_with_login(login):
    '''Select every row that contains given login/email'''

    try:
        connection = create_connection()
        cursor = connection.cursor()
        print(Fore.GREEN + 'Connected websites: ')
        table = PrettyTable(['ADDRESS','LOGIN','PASSWORD','DESCRIPTION'])
        for row in cursor.execute("SELECT * FROM users_table WHERE login=(?)", (login,)):
            table.add_row(row)
        print(table)
        print(Style.RESET_ALL)
    except sqlite3.ProgrammingError as error:
        print(Fore.RED + "Selection error: " + Style.RESET_ALL)
        print(error)

def show_auth_data_for_app(app):
    '''Select every row that contains given web/app name'''

    try:
        connection = create_connection()
        cursor = connection.cursor()
        print(Fore.GREEN + f'Authentication data for {app}: ')
        table = PrettyTable(['ADDRESS','LOGIN','PASSWORD','DESCRIPTION'])
        for row in cursor.execute('SELECT * FROM users_table WHERE domain=(?)', (app,)):
            table.add_row(row)
        print(table)
        print(Style.RESET_ALL)
    except sqlite3.ProgrammingError as error:
        print(Fore.RED + "Selection error: " + error + Style.RESET_ALL)

def add_new_row(site, login, password, description):
    '''Add new record'''

    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users_table VALUES (?, ?, ?, ?)",
                        [site, login, password, description])
        connection.commit()
        print(Fore.GREEN + "Record added successfully" + Style.RESET_ALL)

    except sqlite3.ProgrammingError as error:
        print(Fore.RED + 'Problem occurr while')
        print(error)

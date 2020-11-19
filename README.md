# Simple Password Manager

## About:

First of all, I completely advise against using this script to store sensitive and confidential data.
It has been created in order to practice the separation of functionality into individual modules and communication with the database using the sqlite3.
The database created with the script has no security and the passwords stored in it are not encrypted in any way.
(You can easily access data opening the database with notepad)

## How To Install:

Soo, at first you need to install Python version 3.7.x or older. 
You can simply achive that by visiting: https://www.python.org/

Using pip (installed with python by default) you need to download one module manualy, because it's not not defaultly installed with others.

'''sh
pip install colorama
'''

## How To Run Program

To run script launch main.py. After first attempt to connect to database, 
if it doesn't exist already, then the script will create manager database.db file in the same directory.

The program supports text coloring, but some types of encoding may have problems with it.

In database there is only one table called users_table with columns: domain, login, password, description. (all text)

## Release History

* 1.0.0 (19.11.2020)
    * First release

## Meta

Kamil Graczyk - [@Twitter](https://twitter.com/xor_toja) - graczyk53@gmail.com
Distributed under the ___ license. See ''LICENSE'' for more information.

[https://github.com/xorToja](https://github.com/xorToja)

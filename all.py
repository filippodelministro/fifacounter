
import sys
import os
import sqlite3


# maybe useless
class pswd_object:
    def __init__(self, service, password):
        self.service = service
        self.password = password

pswd_list = []   # list of pswd_objects


# -----------------------------------------------
#                  UTILITY FUNCTIONS
# ----------------------------------------------- 

# def init():
    # todo: initialize the DB for user, matches ecc.
    # conn = sqlite3.connect('password.db')
    # cursor = conn.cursor()

    # conn.commit()
    # conn.close()

def prompt():
    print(">", end='')

# ----------------------------------------------- 
#                  COMMANDS FUNCTIONS
# ----------------------------------------------- 

def help_command():
    print("Try any of the following commands:\n\n"
        "1) help: show commands details\n"
        "2) list: show all passwprd list\n"
        "3) save: save new password\n"
    )

def boot_command():
    print("Welcome in fifacounter!\n")
    help_command()

def esc_command():
    exit(0)

def list_command():
    print("\t#\tname\t\tpassword\n")

    i = 1
    for obj in pswd_list:
        print("\t" + str(i) + "\t" + obj.service + "\t\t" + obj.password)
        i += 1

def save_command():
    ok = False

    serv = input("Insert service you want to save a password for: \n")
    #todo: check for similar services and prompt it
    for obj in pswd_list:
        if obj.service == serv:
            print("password already register for this service")
            #todo: add "modify password" option

            return

    #!fix 
    psw = input("password: ")
    confirm = input("password confirm: ")

    if psw == confirm:
        pswd_list.append(pswd_object(serv, psw))
    else:
        print("password dont match: retry\n")


def clear_command():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def read_command():
    prompt()
    cmd = input()

    if cmd in ("clear", "cls"):
        clear_command()
    elif cmd == "esc":
        esc_command()
    elif cmd == "help":
        help_command()
    elif cmd == "list":
        list_command()
    elif cmd == "save":
        save_command()
    else:
        print("Command not found!\n")
        help_command()
        
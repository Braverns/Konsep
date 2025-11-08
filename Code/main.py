from data import *
from login import *
from menu import *
from InquirerPy import inquirer

def main_menu():
    while True:
        choice = menu()
        os.system('cls || clear')

        if choice == f"|{'1. Master':<{105}}|":
            login('admin')
            input('Enter untuk kembali... ')
        elif choice == f"|{'2. Murid':<{105}}|":
            login('user')
            input('Enter untuk kembali... ')
        elif choice == f"|{'3. Daftar Sebagai Murid':<{105}}|":
            register_user()
            input('Enter untuk kembali... ')
        else:
            print('Goodbye')
            break

main_menu()

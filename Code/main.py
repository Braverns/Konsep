from data import *
from login import *

def main_menu():
    while True:
        print('\n=== MENU UTAMA ===')
        print('1. Login Admin')
        print('2. Login User')
        print('3. Daftar User')
        print('4. Keluar')
        choice = input('Pilih: ').strip()
        if choice == '1':
            admin_username = login('admin')
            if admin_username:
                print('op')
        elif choice == '2':
            username = login('user')
            if username:
                print('po')
        elif choice == '3':
            register_user()
        elif choice == '4':
            print('Keluar program.')
            break
        else:
            print('Pilihan tidak valid.')

main_menu()

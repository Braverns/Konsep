from data import *
from login import *

def login(x):
    while True:
        username = input('Admin Username: ').strip()
        password = input('Password: ').strip()
        user = users_db.get(username)
        if user and user['password'] == password and user['role'] == x:
            print(f'Login berhasil! Welcome {username}')
            return username
        else:
            print('Username/password salah')

def register_user():
    while True:
        username = input('Username baru: ').strip()
        if not username:
            print('Username tidak boleh kosong.')
            continue
        if username in users_db:
            print('Username sudah ada. Coba yang lain.')
            continue

        password = input('Password baru: ').strip()
        if not password or ' ' in password or username == password or password.isdigit() or len(password) < 8 or len(password) > 64:
            print('Password tidak boleh kosong.')
            continue
        confirm = input('Ulangi password: ').strip()
        if password != confirm:
            print('Password tidak cocok. Coba lagi.')
            continue

        namat = input('Nama toko: ').strip()
        break

    users_db[username] = {
        'password': password,
        'role': 'user',
        'gold': 1000,
        'data': {'toko': {'nama': namat, 'stock': ''}}
    }
    print(f'User "{username}" berhasil didaftarkan!')

"""
Напишіть сервер, який би отримував у користувача фразу, а потім
надсилав би підраховану кількість слів у відповідь
"""
import socket

def server_program():
    # отримати ім'я хоста
    host = socket.gethostname()
    port = 5000  # ініціювати порт вище 1024

    server_socket = socket.socket()  # створити TCP-сокет
    server_socket.bind((host, port))  # прив’язати сокет до вказаної нами адреси

    # налаштуйте, скільки клієнтів сервер може слухати одночасно
    server_socket.listen(2)
    conn, address = server_socket.accept()  # прийняти нове підключення
    print("Connection from: " + str(address))
    while True:
        # отримати потік даних. Він не приймає пакети даних, більші за 1024 байти
        data = conn.recv(1024).decode()
        if not data:
            # якщо дані не отримані, розрив
            break
        print("from connected user: " + str(data))
        # підрахована кількість слів
        data = bytes(str(len(data.split())), "ascii")
        conn.send(data)  # відправити дані клієнту

    conn.close()  # закрийте з'єднання

if __name__ == '__main__':
    server_program()
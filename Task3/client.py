import socket

def client_program():
    host = socket.gethostname()  # оскільки обидва коди працюють на одному ПК
    port = 5000  # номер порту сервера сокетів

    client_socket = socket.socket()  # створити екземпляр
    client_socket.connect((host, port))  # підключитися до сервера

    message = input(" -> ")  # приймати вхідні дані

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # відправити повідомлення
        data = client_socket.recv(1024).decode()  # отримати відповідь

        print('Number of words in a message: ' + data)  # показати в терміналі

        message = input(" -> ")  # знову введіть дані

    client_socket.close()  # закрийте з'єднання


if __name__ == '__main__':
    client_program()
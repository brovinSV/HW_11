"""
Додайте до серверу з першого завдання функцію чат-боту, який би
відсилав клієнту задані відповіді на певні повідомлення.
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/chatbot", methods=['POST', 'GET'])
def chatbot():
    req = request.get_json()
    client_message = req['message']

    if client_message == 'Hello':
        return 'Hello'
    elif client_message == 'How are you?':
        return 'Things are going great'
    elif client_message == 'Is it difficult to program in Python?':
        return 'Not very difficult'
    else:
        return 'Bye'

app.run(host='127.0.0.1', port=5000)
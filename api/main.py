from flask import Flask, jsonify, request

from api.handler import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return {
        'data': 'Hello World',
    }


@app.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    response = []
    for user in users:
        user_data = {
            'id': user[0],
            'name': user[1],
            'role': user[2],
        }
        response.append(user_data)
    return {
        'data': response,
    }


@app.route('/create-user', methods=['POST'])
def create():
    body = request.get_json()
    response = create_user(body)
    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

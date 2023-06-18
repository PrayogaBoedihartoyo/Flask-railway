from urllib.parse import urlparse
from flask import Flask, request
import psycopg2

app = Flask(__name__)


def connection():
    result = urlparse("postgresql://postgres:7L2HKhn.gDa=+gu@db.pyqnqrabgkadhwuwxkat.supabase.co:5432/postgres")
    conn = psycopg2.connect(
        host=result.hostname,
        port=result.port,
        database=result.path[1:],
        user=result.username,
        password=result.password
    )
    return conn


def get_all_users():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def get_user(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    conn.close()
    return user


def create_user(body):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, role) VALUES (%s, %s)", (body['name'], body['role']))
    conn.commit()
    conn.close()
    return {
        'status': 200,
        'message': 'User created successfully',
    }


def delete_user(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return {
        'status': 200,
        'message': 'User deleted successfully',
    }


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


@app.route('/delete-user/<id>', methods=['DELETE'])
def delete(id):
    check_user = get_user(id)
    if check_user:
        response = delete_user(id)
    else:
        response = {
            'status': 404,
            'message': 'User not found',
        }
    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

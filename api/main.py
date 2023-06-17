from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)


def get_all_users():
    conn = psycopg2.connect(
        host="db.pyqnqrabgkadhwuwxkat.supabase.co",
        port="5432",
        database="postgres",
        user="postgres",
        password="7L2HKhn.gDa=+gu"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def create_user(body):
    conn = psycopg2.connect(
        host="db.pyqnqrabgkadhwuwxkat.supabase.co",
        port="5432",
        database="postgres",
        user="postgres",
        password="7L2HKhn.gDa=+gu"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, role) VALUES (%s, %s)", (body['name'], body['role']))
    conn.commit()
    conn.close()
    return {
        'status': 200,
        'message': 'User created successfully',
    }


def delete_user():
    # conn = psycopg2.connect(
    #     host="db.pyqnqrabgkadhwuwxkat.supabase.co",
    #     port="5432",
    #     database="postgres",
    #     user="postgres",
    #     password="7L2HKhn.gDa=+gu"
    # )
    # cursor = conn.cursor()
    # cursor.execute("DELETE FROM users WHERE id = 1")
    # conn.commit()
    # conn.close()
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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

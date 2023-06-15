import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


def get_all_users():
    conn = psycopg2.connect(
        host="containers-us-west-186.railway.app",
        port="7559",
        database="railway",
        user="postgres",
        password="555UJAEN55s8FUQaEBuT"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def create_user():
    conn = psycopg2.connect(
        host="containers-us-west-186.railway.app",
        port="7559",
        database="railway",
        user="postgres",
        password="555UJAEN55s8FUQaEBuT"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, role) VALUES ('John Doe', 'admin')")
    conn.commit()
    conn.close()
    return {
        'status': 200,
        'message': 'User created successfully',
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
    response = create_user()
    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


def get_all_users():
    conn = psycopg2.connect(
        host="containers-us-west-186.railway.app",
        port="7559",
        database="railway",
        user="postgres",
        password="ks492yYQCJFTYQuSe1u2"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


@app.route('/', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True)

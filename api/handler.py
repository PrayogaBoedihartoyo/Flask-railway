import psycopg2


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

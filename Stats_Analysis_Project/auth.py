import hashlib
from db import get_connection
    
# Auth Helpers
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# auth functions
def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hash_password(password)
    try:
        query = "insert into users (username, password) values(%s,%s)"
        cursor.execute(query,(username,hashed))
        conn.commit()
        return True
    
    except Exception as e:
        print(e)
        return False
    
    finally:
        cursor.close()
        conn.close()

# Login Function
def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hash_password(password)
    query = "select * from users where username = %s and password = %s"
    cursor.execute(query,(username,hashed))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
from flask import Flask, request, jsonify, g
from flask_cors import CORS
import sqlite3
from proximity import calculate_proximity

app = Flask(__name__)
CORS(app)

DATABASE = 'user_database/users.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    cur.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    nric = data.get('nric')
    password = data.get('password') #any password works
    
    print(f"Received login request for NRIC: {nric}")

    user = query_db('SELECT * FROM users WHERE nric = ?', [nric], one=True)
    
    if user:
        db_nric, name, age, postal, phone, prev_matched = user
        print(f"Found user: {name}, NRIC: {db_nric}")
        print(user)
        return jsonify({'nric': nric, 'name': name, 'age': age, 'postal': postal,'phone':phone, 'prev_matched': prev_matched}), 200
    else:
        print("User not found")
        
    return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/api/errands', methods=['GET'])
def get_errands():
    user_postcode = request.args.get('user_postcode')  # Assuming user postcode passed as query parameter
    user_prev_matched = request.args.get("user_prev_matched")
    try:
        conn = sqlite3.connect('errands_database/errands.db')
        c = conn.cursor()
        c.execute('SELECT id, postal_code, tag, description, errand_duration FROM errands')
        errands = c.fetchall()
        conn.close()

        # Convert fetched data to a list of dictionaries with calculated proximity
        errands_list = []
        for errand in errands:
            errand_id, errand_postcode, tag, description, duration = errand
            
            # Calculate proximity (dummy function)
            proximity = calculate_proximity(user_postcode, errand_postcode)
            
            if proximity is not None:
                errand_dict = {
                    'id': errand_id,
                    'proximity': proximity,
                    'description': description,
                    'tag': tag,
                    'duration': duration
                }
                errands_list.append(errand_dict)
        #key = pref_sort(user_prev_matched,errands_list)
        print(user_prev_matched)
        print(errands_list)
        key, errands_list = zip(*sorted(zip(key, errands_list)))
        return jsonify(errands_list)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    return jsonify({'error': 'Failed to fetch errands'}), 500





if __name__ == '__main__':
    with app.app_context():
        conn = get_db()
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                nric TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                postal TEXT NOT NULL,
                phone INTEGER NOT NULL,
                cpf_oa REAL NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
    app.run(debug=True)

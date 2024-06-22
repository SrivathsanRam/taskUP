import sqlite3
import ast  # Library for literal string evaluation

# Function to convert string representation of list to actual list
def str_to_list(s):
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        return []

# Function to convert list to string representation
def list_to_str(lst):
    return str(lst)

# Connect to the SQLite database
conn = sqlite3.connect('user_database/users.db')
cur = conn.cursor()

# Enable foreign key constraints
cur.execute('PRAGMA foreign_keys = ON;')

# Create the users table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        nric TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        postal TEXT NOT NULL,
        phone TEXT NOT NULL,
        prev_matched TEXT
    )
''')

#pick-up, cleaning, gardening, lend tools, share food
sample_data = [
    ('T0454321B', 'Sri', 19, '520828', '91159829', '[ [5, 3, "pick-up"], [5, 2, "lend tools"], [5, 1, "gardening"], [5, 2, "share food"], [5, 0, "cleaning"], [5, 2, "pick-up"], [5, 1, "lend tools"], [5, 0, "gardening"], [5, 3, "share food"], [5, 2, "cleaning"] ]'),
    ('T0412345C', 'Balaji', 19, '520829', '82923307', '[ [30, 5, "gardening"], [20, 5, "gardening"], [20, 6, "gardening"], [20, 4, "gardening"], [20, 3, "gardening"], [20, 0, "gardening"], [20, 1, "gardening"] ]')
]

# Insert or update sample data
for data in sample_data:
    nric, name, age, postal, phone, prev_matched_str = data
    cur.execute('''
        INSERT OR REPLACE INTO users (nric, name, age, postal, phone, prev_matched)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nric, name, age, postal, phone, prev_matched_str))

# Commit the transaction
conn.commit()

# Fetch and print the data to verify insertion
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row[0], row[1], row[2], row[3], row[4], str_to_list(row[5]))  # Convert prev_matched from string to list

# Close the connection
conn.close()

import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('errands_database/errands.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Create the errands table
cur.execute('''
    CREATE TABLE IF NOT EXISTS errands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        postal_code TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        tag TEXT NOT NULL,
        description TEXT NOT NULL,
        errand_duration INTEGER NOT NULL
    )
''')

# Sample data points
sample_data = [
    ('520828', '91159829', 'cleaning','need help cleaning my gate at #05-113', 5),
    ('520821', '91111111', 'pick-up','need help to pick up buns from blk 824 corner shop. will collect at lift lobby', 10),
    ('520829', '92222222', 'gardening','need help watering my snake plant at #07-154', 5),
    ('520826', '933333333', 'share food','would appreciate any food for dinner tonight. collect at lift lobby', 10),
    ('520813', '94444444', 'gardening','need help watering and pruning my hydrangeas and roses at #02-128', 20)
]

# Insert sample data into the errands table
cur.executemany('''
    INSERT INTO errands (postal_code, phone_number, tag, description, errand_duration)
    VALUES (?, ?, ?, ?, ?)
''', sample_data)

# Commit the transaction
conn.commit()

# Fetch and print the data to verify insertion
cur.execute('SELECT * FROM errands')
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()

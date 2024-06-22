import pandas as pd
import sqlite3


csv_file_path = 'database/users.csv'


df = pd.read_csv(csv_file_path)

df['age'] = df['age'].astype(int)
df['cpf_oa'] = df['cpf_oa'].astype(float)


db_path = 'database/users.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    nric TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    postal TEXT NOT NULL,
    cpf_oa REAL NOT NULL
)
"""
cursor.execute(create_table_query)
conn.commit()

# Insert data from DataFrame to SQLite table
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO users (nric, name, age, postal, cpf_oa)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(insert_query, (row['nric'], row['name'], row['age'], row['postal'], row['cpf_oa']))
    conn.commit()

# Close the database connection
conn.close()

print("Data inserted successfully into the SQLite database.")

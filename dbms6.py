import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ashu27',
    database='ash'
)

# Create a cursor to interact with the database
cursor = connection.cursor()

# Function to create a table if it doesn't exist
def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
    """
    cursor.execute(create_table_query)
    connection.commit()

# Function to add a new record to the table
def add_record(name, age):
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    connection.commit()

# Function to delete a record by ID
def delete_record(user_id):
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()

# Function to update a record by ID
def update_record(user_id, new_name, new_age):
    query = "UPDATE users SET name = %s, age = %s WHERE id = %s"
    cursor.execute(query, (new_name, new_age, user_id))
    connection.commit()

# Function to fetch all records
def fetch_all_records():
    query = "SELECT * FROM users"
    cursor.execute(query)
    return cursor.fetchall()

# Create the table if it doesn't exist
create_table()

# Example usage
add_record("John", 25)
update_record(1, "Johnny", 26)
delete_record(2)
records = fetch_all_records()
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
connection.close()

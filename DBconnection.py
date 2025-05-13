import mysql.connector

# Connect to the databa
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lgu sc&d"
)
cursor = mydb.cursor()

# Step 1: Create the student table
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(100)
);
"""
cursor.execute(create_table_query)

# Step 2: Insert dummy data
insert_query = """
INSERT INTO student (name, age, gender, email)
VALUES (%s, %s, %s, %s)
"""

dummy_data = [
    ("Ali Khan", 21, "Male", "ali.khan@example.com"),
    ("Sara Ahmed", 22, "Female", "sara.ahmed@example.com"),
    ("John Doe", 20, "Male", "john.doe@example.com"),
    ("Fatima Noor", 23, "Female", "fatima.noor@example.com"),
    ("Ahmed Raza", 24, "Male", "ahmed.raza@example.com")
]

cursor.executemany(insert_query, dummy_data)
mydb.commit()
print(f"{cursor.rowcount} rows inserted.\n")

# Step 3: Fetch and display data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

print("Student Data:")
print("ID | Name         | Age | Gender | Email")
print("-" * 50)
for row in rows:
    print(f"{row[0]:<2} | {row[1]:<12} | {row[2]:<3} | {row[3]:<6} | {row[4]}")

# Close connection
cursor.close()
mydb.close()
import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()

# Insertion function
def insert_student(name, age):
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"Inserted: {name}, Age: {age}")

# Update function
def update_student(student_id, new_name):
    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (new_name, student_id))
    conn.commit()
    print(f"Updated ID {student_id} to name: {new_name}")

# Deletion function
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Deleted student with ID: {student_id}")

# Display all records
def display_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\nAll Students:")
    for row in records:
        print(row)

# Example usage
insert_student("GAURAV KUMAR ", 21)
insert_student("PIYUSH", 22)
update_student(1, "PRIYANKA")
delete_student(2)
display_students()

# Close connection
conn.close()

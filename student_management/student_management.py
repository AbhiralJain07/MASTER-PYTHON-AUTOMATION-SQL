import sqlite3
def connect_db():
    return sqlite3.connect("college.db")
def create_table():
    con = connect_db()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        marks INTEGER
    )
    """)
    con.commit()
    con.close()
def add_student():
    name = input("Enter name: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    con = connect_db()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
        (name, course, marks)
    )
    con.commit()
    con.close()
    print("Student added successfully!")
def view_students():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    con.close()

    for row in rows:
        print(row)

def update_marks():
    student_id = int(input("Enter ID: "))
    new_marks = int(input("Enter new marks: "))

    con = connect_db()
    cur = con.cursor()
    cur.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )
    con.commit()
    con.close()

def delete_student():
    student_id = int(input("Enter ID to delete: "))

    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    con.commit()
    con.close()

def search_student():
    student_id = int(input("Enter ID: "))

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cur.fetchone()
    con.close()

    print(student if student else "Not found")

def search_student():
    student_id = int(input("Enter ID: "))

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cur.fetchone()
    con.close()

    print(student if student else "Not found")

def main_menu():
    create_table()

    while True:
        print("""
1. Add Student
2. View Students
3. Update Marks
4. Delete Student
5. Search Student
6. Exit
        """)
        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main_menu()

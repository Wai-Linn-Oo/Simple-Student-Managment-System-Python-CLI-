from db_connection import get_connection
from tabulate import tabulate

class Student:

    def __init__(self, name, age, email, course):
        self.name = name
        self.age = age
        self.email = email
        self.course = course

    def add_student(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            sql = "INSERT INTO students (name, age, email, course) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.name, self.age, self.email, self.course))
            conn.commit()
            print(f"Student added successfully! Roll No: {cursor.lastrowid}")

        except Exception as e:
            print(f"Error adding student: {e}")

        finally:
            
            if cursor: cursor.close()
            if conn: conn.close()
        

    @staticmethod
    def view_students():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(" SELECT * from students ")
        rows = cursor.fetchall()
        if rows:
            print(tabulate(rows, headers=["Roll No", "Name", "Age", "Email", "Course"], tablefmt="psql"))
        else:
            print("No students found!")
        cursor.close()
        conn.close()

    @staticmethod
    def update_student(roll_no):
        if not roll_no:
            print("Roll number required for update!")
            return
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM students WHERE roll_no= %s", (roll_no,))
            student = cursor.fetchone()

            if not student:
                print("No student found with that Roll Number!")
                cursor.close()
                conn.close()
                return
        
            print("\nCurrent Student Info:")
            print(f"Roll No: {student[0]}")
            print(f"1.Name: {student[1]}")
            print(f"2.Age: {student[2]}")
            print(f"3.Email: {student[3]}")
            print(f"4.Course: {student[4]}")

            print("\nWhich field do you want to update?")
            choice = int(input("Enter choice (1-4): "))

            match choice:
                case 1:
                    column = "name"
                    new_value = input("Enter new name: ")
                case 2:
                    column = "age"
                    new_value = int(input("Enter new age: "))
                case 3:
                    column = "email"
                    new_value = input("Enter new email: ")
                case 4:
                    column = "course"
                    new_value = input("Enter new course: ")
                case _:
                    print("Invalid choice!")
                    cursor.close()
                    conn.close()
                    return
        
            sql = f"UPDATE students SET {column} = %s where roll_no=%s"
            cursor.execute(sql, (new_value, roll_no))
            conn.commit()
        
            print(f"{column.capitalize()} updated successfully!")

        except Exception as e:
            print(f"Error updating student: {e}")

        finally:
            if cursor: cursor.close()
            if conn: conn.close()

           
    @staticmethod
    def delete_student(roll_no):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM students WHERE roll_no= %s"
        cursor.execute(sql, (roll_no, ))
        conn.commit()
        cursor.close()
        conn.close()
        print("Student deleted successfully!")

    @staticmethod
    def search_students(keyword):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM students WHERE name LIKE %s OR course LIKE %s"
        cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        
        if rows:
            print(tabulate(rows, headers=["Roll No", "Name", "Age", "Email", "Course"], tablefmt="psql"))
        else:
            print("No students found matching that keyword.")
        
        cursor.close()
        conn.close()
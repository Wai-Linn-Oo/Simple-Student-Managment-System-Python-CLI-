from student import Student

def main_menu():
    while True:
        print("---Student Managment System---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student (by name or Course)")
        print("0. Exit")
        choice = int(input("Enter choice: "))

        match choice:

            case 1:
                name = input("Enter student name: ")
                age = int(input("Enter student's age: "))
                email = input("Enter student's email: ")
                course = input("Enter student' course: ")
            
                student = Student(name, age, email, course)
                student.add_student()

            case 2:
                Student.view_students()

            case 3:
                roll_no = int(input("Enter Roll No to update: "))
                Student.update_student(roll_no)

            case 4:
                roll_no = int(input("Enter Roll No to delete: "))
                Student.delete_student(roll_no)

            case 5:
                keyword = input("Enter Name or Course to search: ")
                Student.search_students(keyword)

            case 0:
                print("Exiting...")
                break

            case _:
                print("Invlid Choice!")

if __name__ == "__main__":
    main_menu()
                
                   
        
   

            
        
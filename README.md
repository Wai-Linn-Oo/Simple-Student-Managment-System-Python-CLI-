Student Management System (Python + MySQL)

A simple command-line-based Student Management System built with Python and MySQL.
This project demonstrates CRUD operations (Create, Read, Update, Delete) and integrates a MySQL database with Python for real-world backend logic practice.

Features

✅ Add Student – Insert new student records into the database.
✅ View Students – Display all students in a tabular format.
✅ Update Student – Edit a specific student's details (name, age, email, or course).
✅ Delete Student – Remove a student record by roll number.
✅ Search Students – Search by name or course keyword.
✅ MySQL Integration – Uses a persistent database (sms_simple).
✅ Formatted Output – Uses the tabulate library for clean table display.

Project Structure

student_management_system/
│
├── db_connection.py       # Handles MySQL database connection
├── student.py             # Contains the Student class (CRUD operations)
├── main.py                # Main program (menu interface)
└── README.md              # Project documentation

Requirements

Make sure you have the following installed:

Python 3.8+

MySQL Server

mysql-connector-python (for Python–MySQL connection)

tabulate (for displaying tables)

You can install the dependencies using:

pip install mysql-connector-python tabulate

🧰 Database Setup

Open MySQL and create the database:

CREATE DATABASE sms_simple;


Select the database:

USE sms_simple;


Create the students table:

CREATE TABLE students (
    roll_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100),
    course VARCHAR(100)
);


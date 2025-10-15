# Student Management System (Python + MySQL)

A simple **command-line-based Student Management System** built with **Python** and **MySQL**.  
This project demonstrates **CRUD operations (Create, Read, Update, Delete)** and integrates a **MySQL database** with Python for real-world backend logic practice.

---

## Features

-  **Add Student** – Insert new student records into the database  
-  **View Students** – Display all students in a tabular format  
-  **Update Student** – Edit a specific student's details (name, age, email, or course)  
-  **Delete Student** – Remove a student record by roll number  
-  **Search Students** – Search by name or course keyword  
-  **MySQL Integration** – Uses a persistent database (`sms_simple`)  
-  **Formatted Output** – Uses the `tabulate` library for clean table display  

---

## Requirements

Make sure you have the following installed:

- **Python 3.8+**
- **MySQL Server**
- **mysql-connector-python**
- **tabulate**

Install the required packages using:

```bash
pip install mysql-connector-python
```
If you’re using Python 3 specifically, you can also try:

```bash
pip3 install mysql-connector-python
```
Install tabulate to display data in nicely formatted tables in the terminal.
```bash
pip install mysql-connector-python tabulate
```

## Database Setup

Follow these steps to set up the MySQL database for the project:

1. **Open MySQL Command Line** or a GUI tool such as **phpMyAdmin** or **MySQL Workbench**.

2. **Create the database**:
   ```sql
   CREATE DATABASE sms_simple;

   USE sms_simple;

   CREATE TABLE students (
    roll_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    email VARCHAR(100),
    course VARCHAR(100)
    );

    ```
## How to Run the Project

1.  **Clone or download** this repository.

2. **Open the project folder** in **VS Code** or any IDE of your choice.

3. **Check and update** the database connection in `db_connection.py` according to your MySQL setup:

   ```python
   host = "localhost"
   user = "root"
   password = ""
   database = "sms_simple"

    ```
6. Run the main program from the terminal:

    ```bash
    python main.py
    ```
    







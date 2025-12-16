# Student Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green?style=flat&logo=qt)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat&logo=sqlite)

A desktop GUI application designed to handle student record management efficiently. Built using Python and PyQt6, this application performs full CRUD (Create, Read, Update, Delete) operations on a local SQLite database, offering a clean and user-friendly interface for educational administrators.

![Application Screenshot](pngs/interaface.png)
## 🚀 Features

* **Dashboard View:** Displays a comprehensive table of all students, including their ID, Name, Course, and Mobile number.
* **Add Student:** dedicated dialog window to insert new student records with specific course selection.
* **Search Functionality:** Real-time search feature to locate specific students by name within the database.
* **Edit Records:** Select any student to update their details (Name, Course, or Contact Info) via a modal dialog.
* **Delete Records:** Secure deletion workflow with confirmation dialogs to prevent accidental data loss.
* **Status Bar Integration:** Dynamic action buttons (Edit/Delete) appear in the status bar when a specific record is selected.

## 🛠️ Technologies Used

* **Language:** Python 3
* **GUI Framework:** PyQt6 (Widgets, Layouts, Dialogs)
* **Database:** SQLite3
* **Architecture:** Object-Oriented Programming (OOP) with modular dialog classes.

## ⚙️ Setup and Installation

### Prerequisites
* Python 3.x installed on your system.
* `pip` package manager.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/student-management-system.git](https://github.com/yourusername/student-management-system.git)
cd student-management-system

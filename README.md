
````markdown
# 📚 Library Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge) 
![SQLite](https://img.shields.io/badge/SQLite-Database-orange?style=for-the-badge) 
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge) 
![Telegram](https://img.shields.io/badge/Telegram-API-blueviolet?style=for-the-badge) 

A **Python-based GUI Library Management System** built with **Tkinter** and **SQLite**.  
This system allows managing books, students, and borrowing records efficiently, with **Telegram reminders** for book returns.

---

## 📖 Table of Contents

- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Telegram API Setup](#telegram-api-setup)  
- [Usage](#usage)  
- [Database Structure](#database-structure)  
- [Project Workflow](#project-workflow)  


---

## ✨ Features

1. **Book Management**  
   - Add new books to the database.  
   - Delete books or reduce available copies.  
   - Search for books by name and author.

2. **Student Management**  
   - Add students borrowing a book with branch, year, ID, and mobile number.  
   - Delete student records when books are returned.  
   - View a dynamic borrow list.

3. **Borrowing System**  
   - Automatically calculates **return dates** (15 days from issue).  
   - Tracks **days left** for returning books.

4. **Notifications**  
   - Sends automated **Telegram messages** to students whose return date is near (2 days remaining).

5. **Real-time Updates**  
   - Scrollable dynamic display of borrowed books and remaining days.

---

## 🛠 Technologies Used

- **Python 3.x**  
- **Tkinter** (GUI)  
- **SQLite** (Database)  
- **Telethon** (Telegram API Integration)  
- **Requests** (Check Internet Connectivity)

---

## ⚙ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
````

2. **Install dependencies**

```bash
pip install tkinter requests telethon
```

3. **Run the application**

```bash
python main.py
```

---

## 📲 Telegram API Setup

To enable Telegram notifications:

1. Create a Telegram app via [my.telegram.org](https://my.telegram.org/).
2. Obtain your **API ID** and **API Hash**.
3. Replace the placeholders in `main.py`:

```python
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = '+91XXXXXXXXXX'  # Include country code
```

4. Ensure the student's mobile number is in **international format**, e.g., `+91XXXXXXXXXX`.
5. Run the program; messages will be sent to students when books are due in 2 days.

---

## 🚀 Usage

1. **Add a New Book**

   * Click **"Add New Book"** → Fill Book Name, Author, Copies → Click **Add**

2. **Delete a Book**

   * Click **Delete Book** → Fill details → Click **Delete**

3. **Add Student Record**

   * Fill Student Name, Branch, Year, ID, Mobile → Select Book → Click **Add to Record**

4. **Delete Student Record**

   * Enter Student ID → Click **Delete Record**

5. **Send Telegram Reminder**

   * Click **Send Message** to notify students about returning books.

6. **Search Books**

   * Enter Book Name and Author → Click **Search**

---

## 🗄 Database Structure

### BookData Table

| Column Name   | Type    | Description                |
| ------------- | ------- | -------------------------- |
| BookName      | VARCHAR | Name of the book (unique)  |
| AutherName    | VARCHAR | Author of the book         |
| numberOfBooks | INT     | Number of available copies |

### studentData Table

| Column Name  | Type    | Description                   |
| ------------ | ------- | ----------------------------- |
| bookName     | VARCHAR | Book borrowed by student      |
| autherName   | VARCHAR | Author of the borrowed book   |
| studentName  | VARCHAR | Name of the student           |
| branch       | VARCHAR | Student branch                |
| year         | VARCHAR | Year of study                 |
| id           | VARCHAR | Student ID                    |
| dateOfReturn | VARCHAR | Date to return book           |
| daysLeft     | INT     | Remaining days to return book |
| mobileNumber | INT     | Student mobile number         |

---

## 🏗 Project Workflow

1. Initialize Tkinter GUI
2. Connect to SQLite and create tables if they don’t exist
3. Add/Delete Books and Manage Student Records via GUI
4. Automatically calculate return dates and days left
5. Send Telegram reminders when return date is near
6. Display dynamic borrow list with scrollable interface

---




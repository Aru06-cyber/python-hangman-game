![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![Python 3](https://img.shields.io/badge/python-3.x-blue.svg)
# 🕹️ Hangman Game (Python + MySQL)

This is a beginner-friendly Hangman game built in Python. The game allows player registration, scoring, and saving best scores using a MySQL database.

## 📌 Features
- Player registration and login
- Word guessing with hangman graphics
- Score tracking (including best score for each player)
- MySQL database integration

## 🛠️ Technologies Used
- Python 3
- MySQL (for storing player data and scores)

## 🚀 How to Run
1️⃣ Ensure you have Python and MySQL installed.  
2️⃣ Create a database named `hangman` and required tables:

```sql
CREATE DATABASE hangman;
USE hangman;

CREATE TABLE Player_Registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE id_player (
    p_id INT
);

CREATE TABLE p_scores (
    p_id INT,
    score INT
);
```
3️⃣ Update the database connection credentials in init_db.py if needed.
4️⃣ Run the game:
```bash
python run_hangman.py
```

📂 Project Structure

├── gameplay.py
├── init_db.py
├── run_hangman.py
└── README.md

⚠️ Note:
This is a personal learning project. Contributions are not accepted at this time.

📄 License

This project is open-source and free to use for educational purposes.

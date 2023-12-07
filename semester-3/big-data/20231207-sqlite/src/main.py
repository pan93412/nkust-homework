import sqlite3

with sqlite3.connect("./test.db") as db:
    # -- create database --
    db.execute((
        "CREATE TABLE IF NOT EXISTS users("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT NOT NULL,"
        "gender TEXT"
        ")"
    ))

    # --- insert data ---
    db.executemany((
        "INSERT INTO users (name, gender) VALUES (?, ?)"
    ), [
        ("王小明", "男"),
        ("王小華", "女"),
        ("王大明", "男"),
        ("王大華", "女"),
        ("王中明", "男"),
        ("王中華", "女"),
        ("王小明", "男"),
        ("王小華", "女"),
        ("王大明", "男"),
        ("王大華", "女"),
        ("王中明", "男"),
        ("王中華", "女"),
    ])
    db.commit()

    # --- select data ---
    cursor = db.cursor()
    result = cursor.execute("SELECT * FROM users")
    for row in result:
        print(row)




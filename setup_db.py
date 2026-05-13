import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Table create
cur.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
)
""")

# Sample data
cur.executemany("""
INSERT INTO employees (name, department, salary, city)
VALUES (?, ?, ?, ?)
""", [
    ("Pooja", "Data", 80000, "Pune"),
    ("Rahul", "IT", 50000, "Mumbai"),
    ("Neha", "Data", 70000, "Pune"),
    ("Amit", "HR", 45000, "Delhi")
])

conn.commit()
conn.close()

print("Database Created Successfully!")
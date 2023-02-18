import csv
from cs50 import SQL

db = SQL("sqlite:///roster.db")

db.execute("INSERT INTO houses(house_name, head) VALUES('Slytherin', 'Severus Snape')")
db.execute("INSERT INTO houses(house_name, head) VALUES('Ravenclaw', 'Filius Flitwick')")
db.execute("INSERT INTO houses(house_name, head) VALUES('Gryffindor', 'Minerva McGonagall')")
db.execute("INSERT INTO houses(house_name, head) VALUES('Hufflepuff', 'Pomona Sprout')")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file);

    for row in reader:
        id, student, house = row["id"], row["student_name"], row["house"]
        db.execute(f"INSERT INTO students(id, student_name) VALUES(\'{id}\', \'{student}\')")
        db.execute(f"INSERT INTO assignments(student_id, house) VALUES(\'{id}\', \'{house}\')")
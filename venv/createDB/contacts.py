import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Raunak', 9967578783, 'palitraunak@johndeere.com')")
db.execute("INSERT INTO contacts VALUES ('Mahesh', 7798900354, 'gotemahesh@johndeere.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

cursor.close()
db.commit()
db.close()
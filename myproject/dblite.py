import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE athletes (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                dob DATE NOT NULL)""")

cursor.execute("""CREATE TABLE TIMING_DATA (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                athlete_id  INTEGER NOT NULL,
                value TEXT NOT NULL,
                FOREIGN KEY (athlete_id) REFERENCES athletes)""")
cursor.execute("INSERT INTO athletes (name, dob)VALUES (?,?)", ('Adrian', '26/03/1987'))

cursor.execute("SELECT * FROM athletes")
res = cursor.fetchall()
for row in res:
    print(row)

cursor.execute("SELECT * FROM athletes WHERE name=? and dob=?", ('Adrian', '26/03/1987'))
the_current_id = cursor.fetchone()
cursor.execute("INSERT INTO TIMING_DATA (athlete_id, value)VALUES (?,?)", (the_current_id[0], '120'))

connection.commit()
connection.close()

cursor.execute("create table log( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
               "ts timestamp default current_timestamp,"
               "phrase TEXT NOT NULL,"
               "letter  TEXT NOT NULL,"
               "ip TEXT NOT NULL,"
               "browser_string TEXT NOT NULL,"
               "results TEXT NOT NULL,"
               "username TEXT NOT NULL,"
               "FOREIGN KEY(username) references players(username))"
               )

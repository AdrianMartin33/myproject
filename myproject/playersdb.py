import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE players (
#                username TEXT UNIQUE NOT NULL,
#                password TEXT NOT NULL,
#                statistics TEXT NOT NULL)""")

#cursor.execute("INSERT INTO players (username, password,statistics) VALUES (?,?,?)",
#               ('anonymous', ' ', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'))
#connection.commit()
cursor.execute("DROP table log")
connection.commit()
cursor.execute("create table log(" 
               "timestamp TEXT NOT NULL,"
               "form TEXT NOT NULL,"
               "remoteAdress  TEXT NOT NULL,"
               "userAgent TEXT NOT NULL,"
               "results TEXT NOT NULL,"
               "username TEXT NOT NULL,"
               "FOREIGN KEY(username) references players(username))")

connection.commit()
connection.close()
cursor.close()

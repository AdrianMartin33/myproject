import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'holiboli',
            'database': 'search_log', }

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)

res = cursor.fetchall()
print(res)

_SQL = """describe log"""
cursor.execute(_SQL)

res = cursor.fetchall()
print(res)

for row in res:
    print(row)

_SQL = """select * from log"""
cursor.execute(_SQL)

res = cursor.fetchall()
for row in res:
    print(row)

_SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            ('galaxia','aeiou', '127.0.0.1','Chrome',"{'a','i'}")"""
cursor.execute(_SQL)

_SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s,%s,%s,%s,%s)"""
cursor.execute(_SQL, ('galaxia', 'bcdf', '127.0.0.1', 'Chrome', 'set()'))

conn.commit()  # Hasta que no hagamos el commit no está en la base de datos
cursor.close()
conn.close()

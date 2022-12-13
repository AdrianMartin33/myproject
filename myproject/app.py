import sqlite3
from html import escape

from flask import Flask, render_template, request
from search4web import search4letters, log_request
import mysql.connector

app = Flask(__name__)
app.config["DEBUG"] = True

# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#    username="Amartin3",
#    password="hellowworld",
#    hostname="Amartin3.mysql.pythonanywhere-services.com",
#    databasename="the database name you chose, probably yourusername$comments",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# @app.route("/")
# def hello() -> '302':
#     return redirect("/entry")


# @app.route("/<name>")
# def hello(name):
#    return f"Hello, {escape(name)}!"

# @app.route("/index")
# def index():
#    return f"Index Page"

letras = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
          'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
          'w': 0, 'x': 0, 'y': 0, 'z': 0
          }


@app.route("/results", methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    username = request.form['username']
    letters = letters.split(sep=',')
    result = ""
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()
    cursor.execute("""SELECT* FROM players WHERE username = ?""", (username,))
    res = cursor.fetchall()
    stat_temp = res[0]
    stat = stat_temp[2]
    stat = stat.split(sep=',')
    print(stat)
    for i in letters:
        result = result + str(search4letters(phrase, i)) + " "
    i = 0
    for j in letras.keys():
        letras[j] = stat[i]
        i = i + 1

    for conjunto in result:
        for letter in conjunto:
            if letter.isalpha():
                letras[letter] = int(letras[letter]) + 1
    valores = ""
    for each in letras.values():
        valores = valores + str(each) + ","
    print(letras.values())
    print(valores)
    cursor.execute(
        """UPDATE players SET statistics=""" + "'" + valores + "'" + """ WHERE username=""" + "'" + username + "'")
    connection.commit()
    cursor.close()
    connection.close()
    #sorteddictwithvalues = dict(sorted(letras.items(), key=lambda x: x[1], reverse=True))

    log_request(request, result, username)
    return render_template('results.html',
                           the_title='Here are your results:',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=result,
                           the_username=username,
                           the_statistics=letras)


@app.route("/search", methods=['POST'])
def entry_page():
    username = request.form['username']
    password = request.form['password']
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM players WHERE username = ?  and password = ?""", (username, password))
    res = cursor.fetchall()
    cursor.close()
    connection.close()
    if not res:
        return render_template('login.html',
                               the_title='Username or password incorrect, try again!')
    else:
        return render_template('entry.html',
                               the_username=username,
                               the_title='Welcome to search  letters on the web ' + username + '!')


@app.route("/search2", methods=['POST'])
def entry_page2():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()
    if password == password2:
        cursor.execute("""SELECT* FROM players WHERE username = ?""", (username,))
        res = cursor.fetchall()
        if not res:
            cursor.execute("""insert into players (username,password,statistics) VALUES (?,?,?)""",
                           (username, password, '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'))
            connection.commit()
            return render_template('entry.html',
                                   the_username=username,
                                   the_title='Welcome to search  letters on the web and thanks for registering!')
        else:
            return render_template('register.html',
                                   the_title='Username already in use, try another')
    elif password != password2:
        return render_template('register.html',
                               the_title='Passwords where not equals, try again')
    cursor.close()
    connection.close()


@app.route("/search3", methods=['POST'])
def entry_page3():
    print('aqui')
    username = request.form['username']
    return render_template('entry.html',
                           the_username=username,
                           the_title='Welcome to search  letters on the web ' + username + '!')


@app.route('/viewlog')
def view_the_log() -> str:
    log = open('vsearch.log', 'r')
    contents = log.read()
    log.close()
    return escape(contents)


@app.route('/')
@app.route("/index")
def index_page():
    return render_template('index.html',
                           the_title='Welcome to search  letters on the web!')


@app.route('/login', methods=['POST'])
def login_page():
    return render_template('login.html',
                           the_title='Welcome to search  letters on the web!')


@app.route('/register', methods=['POST'])
def register_page():
    return render_template('register.html',
                           the_title='Welcome to search  letters on the web!')


@app.route('/anonymous', methods=['POST'])
def anonymous_page():
    return render_template("welcome.html",
                           the_title='Welcome to search  letters on the web for anonymous!',
                           the_username='anonymous')

from html import escape

from flask import Flask, render_template, request
from search4web import search4letters, log_request

app = Flask(__name__)

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
    letters = letters.split(sep=',')
    result = ""
    for each in letters:
        result = result + str(search4letters(phrase, each)) + " "

    for conjunto in result:
        for letter in conjunto:
            if letter.isalpha():
                letras[letter] = letras[letter] + 1

    sortedDictWithValues = dict(sorted(letras.items(), key=lambda x: x[1], reverse=True))

    log_request(request, result)
    return render_template('results.html',
                           the_title='Here are your results:',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=result,
                           the_statistics=sortedDictWithValues)


@app.route("/search", methods=['POST'])
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to search  letters on the web!')


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
                           the_username='You are playing on anonymous mode')

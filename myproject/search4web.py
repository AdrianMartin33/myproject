import datetime
import sqlite3


def search4vowels(word: str) -> set:
    """ Return any vowels found in word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Return any letters found in phrase """
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str, username: str) -> None:
    """ Logger for web operations"""
    log = open("vsearch.log", 'a')
    print(req.form, req.remote_addr, req.user_agent, res, str(datetime.datetime.today()), file=log, sep='|')
    log.close()
    connection = sqlite3.connect('coachdata.sqlite')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO log (username,form,remoteAdress,userAgent,results,timestamp) VALUES (?,?, ?, ?, ?, ?)", (username, str(req.form), str(req.remote_addr), str(req.user_agent), res, str(datetime.datetime.today())))
    connection.commit()
    cursor.close()
    connection.close()


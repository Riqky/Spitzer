import sqlite3
import os
import os.path
from sqlite3 import Error

conn = None

def openconn():
    global connection

    try:
        if not os.path.isfile(os.getcwd + 'result.db'):
            print('db file not found, creating')
        connection = sqlite3.connect(os.getcwd + 'result.db')
        print('db connection set')

    except Error as e:
        print('ERROR:')
        print(e)


def createtables():
    queryHost
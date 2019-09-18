from core.config import config
from core.result import export

import sqlite3
import os
import os.path
from sqlite3 import Error

conn = None

#TODO fix!

def test():
    openconn()
    createtables()
    writeresult(export.results)

def openconn():
    global conn

    try:
        if not os.path.isfile(os.getcwd() + '/result.db'):
            print('db file not found, creating: ' + os.getcwd() + '/result.db')
        conn = sqlite3.connect(os.getcwd() + '/result.db')
        print('db connection set')

    except Error as e:
        print('ERROR:')
        print(e)


def createtables():
    queries = config.getData('queries')
    for key, query in  queries.items():
        executequery(query)


def writeresult(result):
    for host, value in result.items():
        query = 'INSERT INTO host(ip) VALUES(\''+host+'\')'
        hostid = executequery(query)

        if 'findings' in value:
            for find in value['findings']:
                query = 'INSERT INTO finding(hostid, find) VALUES(?,?)'
                executequery(query, [hostid, find])

        if 'webpages' in value:
            for page in value['webpages']:
                query = 'INSERT INTO webpage(hostid, page) VALUES(?,?)'
                executequery(query, [hostid, page])


def executequery(query, parameters=None):
    if conn is None:
        print('open connnection first!')
        return
    print(query + '  ' + str(parameters))
    try:
        cur = conn.cursor()
        if parameters is None:            
            cur.execute(query)
        else:
            cur.execute(query, parameters)

        return cur.lastrowid

    except Error as e:
        print(e)
import sqlite3
import os
import os.path
from sqlite3 import Error

from Spitzer.config import config
from Spitzer.result import export
from Spitzer.print import print_error

conn = None

#TODO fix!

def test():
    open_conn()
    create_tables()
    write_result(export.results)

def open_conn():
    global conn

    try:
        if not os.path.isfile(os.getcwd() + '/result.db'):
            print_error('DB file not found, creating: ' + os.getcwd() + '/result.db')
        conn = sqlite3.connect(os.getcwd() + '/result.db')
        print('[-] DB connection set')

    except Error as e:
        print_error('ERROR:' + e)
    except:
        raise


def create_tables():
    queries = config.get_data('queries')
    for query in  queries.items():
        execute_query(query[1])


def write_result(result):
    for host, value in result.items():
        query = 'INSERT INTO host(ip) VALUES(\''+host+'\')'
        hostid = execute_query(query)
        print('host' + str(hostid))

        if 'findings' in value:
            for find in value['findings']:
                query = 'INSERT INTO finding(hostid, find) VALUES(?,?)'
                print('id ' + str(execute_query(query, [hostid, find])))

        if 'webpages' in value:
            for page in value['webpages']:
                query = 'INSERT INTO webpage(hostid, page) VALUES(?,?)'
                print('id ' + str(execute_query(query, [hostid, page])))


def execute_query(query, parameters=None):
    if conn is None:
        print_error('Connection is not open!')
        return
    try:
        cur = conn.cursor()
        if parameters is None:            
            cur.execute(query)
        else:
            cur.execute(query, parameters)

        return cur.lastrowid

    except Error as e:
        print_error('ERROR:' + e)
    except:
        raise
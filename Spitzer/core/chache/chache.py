#chache folder
#this is for temporary files used by the program
#(will be cleared after the program is done)

import os
from shutil import copyfile

def createFile(name, content=''):
    file = open('Spitzer.core/chache/' + name, 'a+')
    file.write(content)

def readFile(name):
    try:
        return open('Spitzer.core/chache/' + name, 'r').read()
    except OSError:
        return ''

def removeFile(name):
    if not os.path.exists('Spitzer.core/chache/' + name):
        os.remove('Spitzer.core/chache/' + name)

def movetocurrent(name):
    src = os.path.realpath('Spitzer.core/chache/' + name)
    dst = os.getcwd() + '/' + name
    copyfile(src, dst)
    print('placed '+name+' in ' + dst)

def clear(): #clears chache on exit
    for file in os.listdir('Spitzer.core/chache'):
        if not file.endswith('.py') and not file.startswith('__pycache__'):
            os.remove('Spitzer.core/chache/' + file)
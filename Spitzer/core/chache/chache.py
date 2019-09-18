#chache folder
#this is for temporary files used by the program
#(will be cleared after the program is done)

import os
from shutil import copyfile

def createFile(name, content=''):
    file = open('lib/chache/' + name, 'a+')
    file.write(content)

def readFile(name):
    try:
        return open('lib/chache/' + name, 'r').read()
    except OSError:
        return ''

def removeFile(name):
    if not os.path.exists('lib/chache/' + name):
        os.remove('lib/chache/' + name)

def movetocurrent(name):
    src = os.path.realpath('lib/chache/' + name)
    dst = os.getcwd() + '/' + name
    copyfile(src, dst)
    print('placed '+name+' in ' + dst)

def clear(): #clears chache on exit
    for file in os.listdir('lib/chache'):
        if not file.endswith('.py') and not file.startswith('__pycache__'):
            os.remove('lib/chache/' + file)
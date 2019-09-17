import os
from shutil import copyfile

def createFile(name, content=''):
    file = open('chache/' + name, 'a+')
    file.write(content)

def readFile(name):
    try:
        return open('chache/' + name, 'r').read()
    except OSError:
        return ''

def removeFile(name):
    if not os.path.exists('chache/' + name):
        os.remove('chache/' + name)

def movetocurrent(name):
    src = os.path.realpath('chache/' + name)
    dst = os.getcwd() + '/' + name
    copyfile(src, dst)
    print('placed '+name+' in ' + dst)

def clear(): #clears chache on exit
    for file in os.listdir('chache'):
        if not file.endswith('.py') and not file.startswith('__pycache__'):
            os.remove('chache/' + file)
#Spitzer/chache folder
#this is for temporary files used by the program
#(will be cleared after the program is done)

import os
from shutil import copyfile
from Spitzer.print import print

path = __file__[:-9]

def createFile(name, content=''):
    file = open(path + name, 'a+')
    file.write(content)

def readFile(name):
    try:
        return open(path + name, 'r').read()
    except OSError:
        return ''

def removeFile(name):
    if not os.path.exists(path + name):
        os.remove(path + name)

def movetocurrent(name):
    src = os.path.realpath(path + name)
    dst = os.getcwd() + '/' + name
    copyfile(src, dst)
    print('[-] Placed '+name+' in ' + dst)

def clear(): #clears Spitzer/chache on exit
    for file in os.listdir(path):
        if not file.endswith('.py') and not file.startswith('__pycache__'):
            os.remove(path + file)
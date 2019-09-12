import os

def createFile(name, content=''):
    file = open('chache/' + name, 'a+')
    file.write(content)

def readFile(name):
    try:
        return open('chache/' + name, 'r').read()
    except OSError:
        return ''

def clear(): #clears chache on exit
    for file in os.listdir('chache'):
        if not file.endswith('.py') and not file.startswith('__pycache__'):
            os.remove('chache/' + file)
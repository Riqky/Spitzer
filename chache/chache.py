#TODO clear chache after exit

def createFile(name, content=''):
    file = open('chache/' + name, 'a+')
    file.write(content)

def readFile(name):
    try:
        return open('chache/' + name, 'r').read()
    except OSError:
        return ''
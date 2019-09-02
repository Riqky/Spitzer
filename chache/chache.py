def createFile(name, content=''):
    file = open('chache/' + name, 'a+')
    file.write(content)

def readFile(name):
    return open('chache/' + name, 'r').read()
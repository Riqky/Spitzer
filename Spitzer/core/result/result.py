result = {}

def addPages(host, pages):
    global result
    check(host)
    result[host]['webpages'] += pages


def add(host, text):
    global result
    check(host)
    result[host]['findings'] += text

def check(host):
    global result
    if host not in result:
        result[host] = {}
        result[host]['findings'] = []
        result[host]['webpages'] = []

def printresult():
    for line in result:
        print(line)

def get():
    return result
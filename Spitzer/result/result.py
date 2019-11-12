from Spitzer.result.export import export_txt

result = {}

def add_pages(host, pages):
    global result
    check(host)
    result[host]['webpages'] += pages


def add(host, title, text):
    global result
    check(host)
    result[host]['findings'] += {title:text}

def check(host):
    global result
    if host not in result:
        result[host] = {}
        result[host]['findings'] = []
        result[host]['webpages'] = []

def export():
    export_txt(result)

def get():
    return result
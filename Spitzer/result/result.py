from Spitzer.result import export_report, export_table

result = {}
hosts = {}

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


def save_hosts(nmap):
    global hosts

    for ip, value in nmap.items():
        hosts[ip] = {}
        for port, val in value['tcp'].items():
            hosts[ip][port] = [val['name'], val['product'], val['version']]

    export_table.export(hosts)
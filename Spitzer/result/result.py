from Spitzer.result import export_report, export_table

import os
import json

result = {}
hosts = {}

def add_vuln(host, vuln):
    global result

    if host in result:
        result[host].append(vuln)
    else:
        result[host] = [vuln]

    print(result)
    print('\n')

def add(host, title, body):
    pass

def add_pages(base_url, pages):
    pass

def export_vulns():
    f = open(os.path.expanduser("~") + '.spitzer_result.json', 'w+')
    f.write(json.dumps(result))
    f.close()

def save_hosts(nmap):
    global hosts

    for ip, value in nmap.items():
        if ip not in hosts:
            hosts[ip] = {}
        for port, val in value['tcp'].items():
            hosts[ip][port] = [val['name'], val['product'], val['version']]

    export_report.export(hosts)
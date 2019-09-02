from scanner import nmapper, masscanner
from chache import chache
from IPy import IP

def sweep(hosts, port):
    masscanner.sweep(hosts, port)
    xml = chache.readFile('sweep.xml')

    if xml is '':
        return

    result = nmapper.parseXml(xml)

    hosts = ''
    for host in result['scan']:
        hosts += ' ' + host

    return hosts

def scanSMB(hosts):
    #TODO maybe check if there are to much hosts
    
    hosts = sweep(hosts, '445')
    if hosts is None:
        return

    return nmapper.scanSMB(hosts)
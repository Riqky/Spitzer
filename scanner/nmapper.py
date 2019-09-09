import nmap
from config import config
import os

nm = nmap.PortScanner()

#TODO maybe change this for big networks
def scan(hosts):
    print('starting nmap')
    result = {}
    for host, ports in hosts.items():
        result[host] = nm.scan(host, stringifyPorts(ports), arguments=config.getDynamic('nmapFlags') + ' oA=' + os.getcwd() + 'scan -Pn', sudo=True)['scan'][host]
    print('nmap done')
    return result


def parseXml(xml):
    result = nm.analyse_nmap_xml_scan(xml)
    if 'error' in result['nmap']['scaninfo']:
        print(result['nmap']['scaninfo']['error'])
        raise RuntimeError
    return result

def stringifyPorts(ports):

    port = ''
    for p in ports:
        port += str(p) + ','

    return port[:-1]
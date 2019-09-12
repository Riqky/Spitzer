import nmap
from config import config
import os

nm = nmap.PortScanner()

#TODO maybe change this for big networks
def scan(hosts):
    print('starting nmap')
    result = {}
    for host, ports in hosts.items():
        script = findScripts(ports)
        arguments = config.getDynamic('nmapFlags') + ' -oN ' + os.getcwd() + '/scan.txt -Pn -sV --script="' + script + '"' #TODO make print with selected verbosity
        result[host] = nm.scan(host, stringifyPorts(ports), arguments=arguments, sudo=True)['scan'][host] 
    print('nmap done')
    return result

def scanSpecific(host, port, arguments):
    return nm.scan(host, stringifyPorts(port), arguments, sudo=True)

def parseXml(xml):
    result = nm.analyse_nmap_xml_scan(xml)
    if 'error' in result['nmap']['scaninfo']:
        print(result['nmap']['scaninfo']['error'])
        raise RuntimeError
    return result

def stringifyPorts(ports):

    port = ''
    if isinstance(ports, list):
        for p in ports:
            port += str(p) + ','
    else:
        return str(ports)

    return port[:-1]

def findScripts(ports):

    result = ''
    scripts = config.getData('ports')

    for port in ports:
        if len(scripts[port]) > 1:
            if scripts[port][1] != '':
                result += scripts[port][1] + ','

    return result[:-1]
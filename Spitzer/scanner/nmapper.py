import nmap
import os

from Spitzer.config import config
from Spitzer.print import print_error
#runs nmap, not much further to say...

nm = nmap.PortScanner()

#TODO maybe change this for big networks
def scan(hosts):
    print('[-] Starting nmap')
    result = {}
    for host, ports in hosts.items():
        script = find_scripts(ports)
        arguments = config.get_dynamic('nmapFlags') + ' -oN ' + os.getcwd() + '/scan.txt -Pn -sV --script="' + script + '"' #TODO make print with selected verbosity
        result[host] = nm.scan(host, stringify_ports(ports), arguments=arguments, sudo=True)['scan'][host]  
    print('[-] Nmap done')

    return result

def scan_specific(host, port, arguments):
    return nm.scan(host, stringify_ports(port), arguments, sudo=True)

def parse_xml(xml):
    result = nm.analyse_nmap_xml_scan(xml)
    if 'error' in result['nmap']['scaninfo']:
        print_error('[!]' + result['nmap']['scaninfo']['error'])
        raise RuntimeError
    return result

def stringify_ports(ports):

    port = ''
    if isinstance(ports, list):
        for p in ports:
            port += str(p) + ','
    else:
        return str(ports)

    return port[:-1]

def find_scripts(ports):

    result = ''
    scripts = config.get_data('ports')

    for port in ports:
        if port not in scripts:
            continue

        if len(scripts[port]) > 1 and scripts[port][1] != '':
            result += scripts[port][1] + ','

    return result[:-1]
import nmap
import os

from Spitzer.config import config
from Spitzer.print import print_error
from Spitzer.command import run
from Spitzer.chache.chache import get_path
#runs nmap, not much further to say...

nm = nmap.PortScanner()

#TODO maybe change this for big networks
'''def scan(hosts):
    print('[-] Starting nmap')
    result = {}
    for host, ports in hosts.items():
        script = find_scripts(ports)
        arguments = config.get_dynamic('nmapFlags') + ' -oN ' + os.getcwd() + '/scan_'+host+'.txt -Pn -sV ' + script #TODO make print with selected verbosity
        try:
            result[host] = nm.scan(host, stringify_ports(ports), arguments=arguments, sudo=True)['scan'][host]  
        except KeyError:
            print_error('[!] Weird KeyError, skipping ' + host)
            #write some data in log
            file = open('/root/error.txt', 'w+')
            file.write(str(file.read()) + '\n' + arguments + ' ' + host + ' ' + ports)
            continue
    print('[-] Nmap done')

    return result'''

def scan(hosts):
    print('[-] Starting nmap')
    print(hosts)
    for host, ports in hosts.items():
        script = find_scripts(ports)
        txt = ['-oN', get_path() + 'scan_' + host + '.txt']
        xml = ['-oX', get_path() + 'scan_' + host + '.xml'] #TODO segmentation fault on large networks
        arguments = ['nmap', config.get_dynamic('nmapFlags'), '-Pn', '-sV', config.get_static('verbosity'), '-p', stringify_ports(ports), host] + txt + xml #TODO change verbosity to 0123

        if script != '':
            arguments.append(script)
        run(arguments)

    return get_results()

def get_results():
    result = {}
    text = ''
    for file in os.listdir(get_path()):
        if file.startswith('scan_') and file.endswith('.xml'):
            xml_result = parse_xml(open(get_path() + file, 'r').read())
            host = file.replace('scan_', '').replace('.xml', '')
            result[host] = xml_result['scan'][host]

        if file.startswith('scan_') and file.endswith('.txt'):
            text +=  open(get_path() + file, 'r').read() + '\n\n'

    open(os.getcwd() + '/scan.txt', 'w+').write(text)
    return  result


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
    if result != '':
        return '--script=' +result[:-1]
    else:
        return ''

import nmap
import os
import multiprocessing
import datetime
import re
import time

from Spitzer.config import config
from Spitzer.print import print_error
from Spitzer import command
from Spitzer.chache.chache import get_path
from Spitzer import interlace
from Spitzer import command
from Spitzer.host import get_hosts, get_ports
#runs nmap, not much further to say...

nm = nmap.PortScanner()

#TODO maybe change this for big networks

'''def run_nmap(ip, ports):
    print('[-] Starting nmap')

    script = find_scripts(ports)
    flags = config.get_config('nmapFlags')

    command = 'nmap ' + flags + ' -Pn -sV '+ports+' _host_ -oX  _output_/_host_.xml -oN _output_/_host_.txt'

    if script != '':
        command += script
    run(command, ip)
    return get_results()

def scan(hosts):
    print('[-] Starting nmap') 

    dic = hosts 
    hosts = get_hosts(dic)
    ports = get_ports(dic)
    script = find_scripts(ports)
    flags = config.get_config('nmapFlags')
    ports = stringify_ports(ports)

    command = 'nmap ' + flags + ' -Pn -sV -p '+ports+' _host_ -oX  _output_/_host_.xml -oN _output_/_host_.txt'

    if script != '':
        command += script

    run(command, hosts)
    return get_results()

def get_results():
    result = {}
    text = ''
    while len(list(filter(re.compile('.xml$').search, os.listdir(get_path())))) != 0: 
        for file in os.listdir(get_path()):
            if file.endswith('.xml') and file != 'sweep.xml':

                xml = open(get_path() + file, 'r').read()
                if 'finished time' not in xml:
                    continue

                xml_result = parse_xml(xml)
                host = file.replace('.xml', '')
                result[host] = xml_result['scan'][host]
                os.remove(get_path() + file)

        time.sleep(5)

    for file in os.listdir(get_path()):
        if file.endswith('.txt'):
                text +=  open(get_path() + file, 'r').read() + '\n\n'

    open(os.getcwd() + '/scan.txt', 'w+').write(text)
    print('[-] Nmap done')
    return  result'''

def run_nmap(ip, ports):
    print('[-] Starting nmap')

    script = find_scripts(ports)
    flags = config.get_config('nmapFlags')

    command = ['nmap', flags, '-Pn', '-sV', ports, ip, '-oX', 
    get_path() + 'scan_'+ip+'.xml','-oN',  get_path() + 'scan_'+ip+'.txt']

    if script != '':
        command += script
    command.run(command, verbose=int(config.get_config('verbose')))
    return get_results()

def scan(hosts):
    print('[-] Starting nmap')
    for host, ports in hosts.items():
        script = find_scripts(ports)
        txt = ['-oN', get_path() + 'scan_' + host + '.txt']
        xml = ['-oX', get_path() + 'scan_' + host + '.xml'] #TODO segmentation fault on large networks?
        arguments = ['nmap', config.get_config('nmapFlags'), '-Pn', '-sV', '-p', stringify_ports(ports), host] + txt + xml

        if script != '':
            arguments.append(script)
        command.run(arguments, verbose=int(config.get_config('verbose')))

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

import xmltodict
import json

from Spitzer import host
from Spitzer.config import config
from Spitzer.chache import chache
from Spitzer.scanner import nmapper, masscanner
from Spitzer.print import print_error

#scanner class to combine the nmap and the masscanner class
#TODO get ip range on startup

def scan():
    #get configurations
    massconf = config.get_dynamic('masscan')
    times = int(massconf['times'])
    rate = massconf['rate']
    hosts = config.get_dynamic('ip')
    scan = config.get_dynamic('ports')

    #scan options:
    #list: all from the exploit list
    #all: all ports
    #top1: top thousand from nmap
    #top10: top tenthousand from nmap
    #or you can add your own ports
    ports = ''
    if scan == 'list':
        port = config.get_data('ports')
        for p in port:
            ports += str(p) + ','
        ports = ports[:-1] #remove last comma
    elif scan == 'all':
        ports = '0-65535'
    elif scan == 'top1':
        ports = '--top-ports 1000'
    elif scan == 'top10':
        ports = '--top-ports 10000'
    else:
        ports = scan

    #run masscan x times
    #get results from masscan and create one list of hosts with ports
    result = {}
    for i in range(times):
        masscanner.scan(hosts, ports, rate)
        xml = chache.read_file('sweep.xml')
        if xml == '':
            print_error('[!] Scan '+str(i+1)+' failed!')
            print_error('[!] Are there any hosts up? Is the interface correct?')
            return

        mass = json.loads(json.dumps(xmltodict.parse(xml, attr_prefix='')))
        result = host.merge(mass, result)
        #TODO remove or empty file to make sure
        
    #run nmap once to confirm scan (masscan has some false positives)
    return nmapper.scan(result)



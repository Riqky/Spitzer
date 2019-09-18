
import xmltodict
import json

from Spitzer.core import host
from Spitzer.core.config import config
from Spitzer.core.chache import chache
from Spitzer.core.scanner import nmapper, masscanner
#scanner class to combine the nmap and the masscanner class

#TODO! scan only once on to much hosts or to big range, cause this method is shit....
def scan():
    #get configurations
    massconf = config.getStatic('masscan')
    times = int(massconf['times'])
    rate = massconf['rate']
    hosts = config.getDynamic('ip')
    scan = config.getDynamic('ports')

    #scan options:
    #list: all from the exploit list
    #all: all ports
    #top1: top thousand from nmap
    #top10: top tenthousand from nmap
    #or you can add your own ports
    ports = ''
    if scan == 'list':
        port = config.getData('ports')
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
    
    print('ports: ' + ports)

    #run masscan x times
    #get results from masscan and create one list of hosts with ports
    result = {}
    for i in range(times):
        masscanner.scan(hosts, ports, rate)
        xml = chache.readFile('sweep.xml')
        if xml == '':
            print('scan '+i+' failed!')#TODO make retry?
            continue

        mass = json.loads(json.dumps(xmltodict.parse(xml, attr_prefix='')))
        result = host.merge(mass, result)
        


    #run nmap once to confirm scan (masscan has some false positives)
    return nmapper.scan(result)



from config import config
from chache import chache
from scanner import masscanner
from scanner import nmapper
import host
import xmltodict
import json

#TODO! scan only once on to much hosts or to big range, cause this method is shit....
def scan():
    hosts = config.getDynamic('ip')

    scanAll = config.getDynamic('scanAll')

    if not isinstance(scanAll, bool):
        print('unreconised opion for scanAll: ' + scanAll)
        print('assuming True')
        scanAll = True

    ports = ''

    if scanAll:
        ports = '0-65535'
    else:
        port = config.getData('ports')
        for p in port:
            ports += str(p) + ','
        ports = ports[:-1] #remove last comma

    #run masscan twice (multithreaded)
    masscanner.scan(hosts, ports)

    #get results from masscan and create one list of hosts with ports
    xml1 = chache.readFile('sweep1.xml')
    xml2 = chache.readFile('sweep2.xml')
    #complete fail if both scan failed
    if xml1 is '' and xml2 is '':
        print('did you set the correct interface?')
        raise RuntimeError('both masscans failed')

    #don't have to merge when one scan failed
    if xml1 is '':
        print('masscan 1 failed, continuing')
        return nmapper.scan(host.extractHostsXML(json.loads(json.dumps(xmltodict.parse(xml2, attr_prefix='')))))
    elif xml2 is '':
        print('masscan 2 failed, continuing')
        return nmapper.scan(host.extractHostsXML(json.loads(json.dumps(xmltodict.parse(xml1, attr_prefix='')))))

    mass1 = json.loads(json.dumps(xmltodict.parse(xml1, attr_prefix='')))
    mass2 = json.loads(json.dumps(xmltodict.parse(xml2, attr_prefix='')))
    hosts = host.merge(mass1, mass2)

    #run nmap once to confirm scan (masscan has some false positives)
    return nmapper.scan(hosts)



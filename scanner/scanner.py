from config import config
from chache import chache
from scanner import masscanner
from scanner import nmapper
import host

#TODO! scan only once on to much hosts or to big range, cause this method is shit....
def scan(hosts):
    port = config.getStatic('ports')

    ports = ''
    for p in port:
        ports += p + ','

    ports = ports[:-1] #remove last comma

    #run masscan twice (multithreaded)
    masscanner.scan()

    #get results from masscan and create one list of hosts with ports
    xml1 = chache.readFile('sweep1.xml')
    xml2 = chache.readFile('sweep2.xml')

    #complete fail if both scan failed
    if xml1 is '' and xml2 is '':
        raise RuntimeError('both masscans failed')

    #don't have to merge when one scan failed
    if xml1 is '':
        print('masscan 1 failed, continuing')
        return nmapper.scan(host.extractHosts(nmapper.parseXml(chache.readFile('sweep1.xml'))))
    elif xml2 is '':
        print('masscan 2 failed, continuing')
        return nmapper.scan(host.extractHosts(nmapper.parseXml(chache.readFile('sweep2.xml'))))

    mass1 = nmapper.parseXml(chache.readFile('sweep1.xml'))
    mass2 = nmapper.parseXml(chache.readFile('sweep2.xml'))

    hosts = host.merge(mass1, mass2)

    #run nmap once to confirm scan (masscan has some false positives)
    return nmapper.scan(hosts)



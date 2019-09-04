import nmap

nm = nmap.PortScanner()

def scanPort(hosts, port, service=None, alias=None):

    if alias is None and service is None:
    
        raise RuntimeError('enter alias or service!')

    if alias is None:
        alias = service

    nm.scan(hosts, port)
    
    hosts = []
    found = False

    for host, value in nm._scan_result['scan'].items():
        #check if 445 is open and is correct service
        if value['tcp'][port]['state'] == 'open' and (value['tcp'][port]['name'] == service or service is None):
            hosts.append([host, value['tcp']])
            print(alias + ' is running on:  ' + host)
            found = True

    if not found:
        print('No hosts found with ' + alias)
        return

    print()
    return hosts

def parseXml(xml):
    result = nm.analyse_nmap_xml_scan(xml)
    if 'error' in result['nmap']['scaninfo']:
        print(result['nmap']['scaninfo']['error'])
        raise RuntimeError
    return result
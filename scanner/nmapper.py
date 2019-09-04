import nmap

nm = nmap.PortScanner()

#TODO maybe change this for big networks
def scan(hosts):
    result = {}
    for host, ports in hosts.items():
        nm.scan(host, ports, sudo=True)
        result[host] = nm._nmap_last_output['scan'][host]

    return result


def parseXml(xml):
    result = nm.analyse_nmap_xml_scan(xml)
    if 'error' in result['nmap']['scaninfo']:
        print(result['nmap']['scaninfo']['error'])
        raise RuntimeError
    return result
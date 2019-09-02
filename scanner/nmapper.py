import nmap

nm = nmap.PortScanner()

def scanSMB(hosts):

    nm.scan(hosts, '445')
    
    hosts = []
    found = False

    for host, value in nm._scan_result['scan'].items():
        #check if 445 is open and is correct service
        if value['tcp'][445]['state'] == 'open' and value['tcp'][445]['name'] == 'microsoft-ds':
            hosts.append(host)
            print('smb is running on:  ' + host)
            found = True

    if not found:
        print('No hosts found with smb')
        return

    print()
    return hosts

def parseXml(xml):
    #TODO check for error
    return nm.analyse_nmap_xml_scan(xml)
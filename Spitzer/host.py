

#to extract the xml files and merge them to one list of hosts

def extract_hosts_nmap(mass):
    result = {}
    for host, value in mass['scan'].items():
        ports = []
        for port in value['tcp']:
            ports.append(port)

        result[host] = ports

    return result

def extract_hosts_xml(mass):
    if 'nmaprun' not in mass:
        return mass

    result = {}
    hosts = mass['nmaprun']['host']

    if not isinstance(hosts, list):
        hosts = [hosts]

    for value in hosts:
        host = value['address']['addr']
        port = value['ports']['port']['portid']

        if host in result:
            result[host].append(port)
        else:
            result[host] = [port]

    return result

def merge(mass1, mass2):
    result1 = extract_hosts_xml(mass1)
    result2 = extract_hosts_xml(mass2)
    missed = {}

    #merge the list of hosts and ports

    for host, ports in result1.items():
        if host not in result2:
            missed[host] = ports
        else:
            ports2 = result2[host]
            merge_ports(missed, ports, ports2, host)

    return merge_missed(result2, missed)


def merge_ports(missed, ports, ports2, host):
    for port in ports:
        if port not in ports2:
            if host in missed:
                missed[host].append(port)
            else:
                missed[host] = [port] 

    return missed

def merge_missed(result, missed):
    for host, ports in missed.items():
        if host in result:
            result[host] += ports
        else:
            result[host] = ports

    return result
#to extract the xml files and merge them to one list of hosts

def extractHosts(mass):
    result = {}
    for host, value in mass['scan'].items():
        ports = []
        for port in value['tcp']:
            ports.append(port)

        result[host] = ports

    return result

def merge(mass1, mass2):
    result1 = extractHosts(mass1)
    result2 = extractHosts(mass2)
    missed = {}

    #TODO? optimise, this code must be able to wirstand 16 millions ip's (maybe)
    #merge the list of hosts and ports

    for host, ports in result1.items():
        if host not in result2:
            missed[host] = ports
        else:
            ports2 = result2[host]
            for port in ports:
                if port not in ports2:
                    if host in missed:
                        missed[host].append(port)
                    else:
                        missed[host] = [port]

    result = result2
    for host, ports in missed.items():
        if host in missed:
            result[host] += ports
        else:
            result[host] = ports

    return result
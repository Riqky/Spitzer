import nmap

nm = nmap.PortScanner()

def getState(host):
    return nm[host]

def scan(host, ports=None, arguments='-sV', sudo=False):
    nm.scan(host, ports, arguments, sudo)
    
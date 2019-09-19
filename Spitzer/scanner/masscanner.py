import subprocess
import threading

from Spitzer.config import config
from Spitzer import command


#runs masscanner twice and writes the output into a xml file in the chache folder
chache = __file__[:-21] + 'chache/' 
def scan(hosts, ports, rate):
    print()
    p = '-p'
    if ports.startswith('-'):
        ports = ports.split(' ')
        p = ports[0]
        ports = ports[1]
    cmd = [
        'masscan',
        hosts,
        '-oX',chache + 'sweep.xml',
        p, ports,
        '-e', config.get_static('interface'),
        '--wait=0',
        config.get_static('verbosity'),
        '--rate=' + rate
        ]

    command.run(cmd)
    
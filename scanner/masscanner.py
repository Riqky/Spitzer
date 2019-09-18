import subprocess
import threading

from config import config
import command

#runs masscanner twice and writes the output into a xml file in the chache folder
#TODO run multiple time

def scan(hosts, ports, rate):
    p = '-p'
    if ports.startswith('-'):
        ports = ports.split(' ')
        p = ports[0]
        ports = ports[1]
    cmd = [
        'masscan',
        hosts,
        '-oX','chache/sweep.xml',
        p, ports,
        '-e', config.getStatic('interface'),
        '--wait=0',
        config.getStatic('verbosity'),
        '--rate=' + rate
        ]

    command.run(cmd)
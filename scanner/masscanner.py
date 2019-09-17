import subprocess
import threading
from config import config
import command

#runs masscanner twice and writes the output into a xml file in the chache folder

def scan(hosts, ports):

    print('started masscan 1')
    cmd = ['masscan', hosts,'-oX', 'chache/sweep1.xml', '-p ' + ports, '-e', config.getStatic('interface'), '--wait=0', config.getStatic('verbosity')]
    one = command.run(cmd)
    print('finished masscan 1')

    print('started masscan 2')
    cmd = ['masscan', hosts,'-oX', 'chache/sweep2.xml', '-p ' + ports, '-e', config.getStatic('interface'), '--wait=0', config.getStatic('verbosity')]
    two = command.run(cmd)
    print('finished masscan 2')

    return [one.stdout, two.stdout] #TODO? restart when one fails
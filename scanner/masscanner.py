import subprocess
import threading
from config import config
import command

#runs masscanner twice and writes the output into a xml file in the chache folder

def scan(hosts, ports):
    '''thread1 = sweepThread(1, hosts, ports, "sweep1.xml")
    thread2 = sweepThread(2, hosts, ports, "sweep2.xml")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()'''

    print('started masscan 1')
    cmd = ['masscan', hosts,'-oX', 'chache/sweep1.xml', '-p ' + ports, '-e', config.getStatic('interface'), '--wait=0']
    command.run(cmd, True)
    print('finished masscan 1')

    print('started masscan 2')
    cmd = ['masscan', hosts,'-oX', 'chache/sweep2.xml', '-p ' + ports, '-e', config.getStatic('interface'), '--wait=0']
    command.run(cmd, True)
    print('finished masscan 2')


class sweepThread(threading.Thread):
    def __init__(self, threadID, hosts, ports, config):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.hosts = hosts
        self.ports = ports
        self.config = config

    def run(self):
        print('started masscan ' + str(self.threadID))
        cmd = ['masscan', self.hosts,'-oX', 'chache/' + self.config, '-p ' + self.ports, '-e', config.getStatic('interface'), '--wait=0']
        command.run(cmd, True)
        print('finished masscan ' + str(self.threadID))
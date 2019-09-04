import subprocess
import threading
from config import config

def scan(hosts, ports):
    thread1 = sweepThread(1, hosts, ports, "sweep1.xml")
    thread2 = sweepThread(2, hosts, ports, "sweep2.xml")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


class sweepThread(threading.Thread):
    def __init__(self, threadID, hosts, ports, config):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.hosts = hosts
        self.ports = ports
        self.config = config

    def run(self):
        #TODO specify interface out of config
        subprocess.run(['masscan', self.hosts,'-oX', 'chache/' + self.config, '-p ' + self.ports, '-e', config.getStatic('interface'), '--wait=0'], capture_output=True, check=True)

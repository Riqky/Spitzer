from zapv2 import ZAPv2
import threading
import subprocess
import shlex
import time
import os

from Spitzer.config import config

###script for the zap API###

#not prefered.....

host = ''
zap = None

def __run():
    #this line means the daemon should be started:
    #[ZAP-daemon] INFO org.zaproxy.zap.DaemonBootstrap  - ZAP is now listening on
    process = subprocess.Popen(['/usr/share/zaproxy/zap.sh', '-daemon'], stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is None:
            #stopped
            raise RuntimeError('error while starting zap')
        if output:
            #print(output.decode('utf-8'), end='')
            finish = '[ZAP-daemon] INFO org.zaproxy.zap.DaemonBootstrap  - ZAP is now listening on'
            error = 'Cannot listen on port '
            if finish in str(output):
                print('zap started succesfully')
                break
            if error in str(output):
                process.terminate()
                print('zap already started')
                break

def exploit(url):
    print('zap')
    init(url)
    methods = config.get_data('zap')
    for method in methods:
        eval(method + '()') 
    #print('error with zap! was the api key correct?') #TODO handle error

def init(this_host):
    global zap
    global host
    host = this_host
    __run()
    zap = ZAPv2(apikey=config.get_static('zapApiKey'))
    zap.urlopen(host)

def spider():
    global host
    print('spidering')
    scanid = zap.spider.scan(host)
    time.sleep(2)
    while(int(zap.spider.status(scanid)) < 100):
        print('Spider progress: ' + zap.spider.status(scanid) + '%', end='\r')
        time.sleep(1)

    print('\nSpider is done!')
    print('\n')
    for host in zap.spider.added_nodes(scanid):
        print(host)

def scan():
    print('zap Scanning')

    scanid = zap.ascan.scan(host)
    print('status' + zap.ascan.status(scanid))
    while(int(zap.ascan.status(scanid)) < 100):
        print('scanning at ' + zap.ascan.status(scanid) + ' %', end='\r')
        time.sleep(1)

    print('\nscan done')


def export():
    html = open(os.getcwd() + '/zapreport.html', 'w+')
    html.write(zap.core.htmlreport())
    html.close() 
    print('created file: ' + os.getcwd() + '/zapreport.html')
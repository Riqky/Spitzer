import subprocess

def sweep(hosts, port):
    #TODO specify interface out of config
    subprocess.run(['masscan', hosts,'-oX', 'chache/sweep.xml', '-p ' + port, '-e', 'tun0', '--wait=0'], capture_output=True)
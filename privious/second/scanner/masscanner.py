import subprocess

def sweep(hosts, port):
    #TODO specify interface out of config
    #TODO catch error(s) (like not 0 on exit)
    subprocess.run(['masscan', hosts,'-oX', 'chache/sweep.xml', '-p ' + port, '-e', 'tun0', '--wait=0'], capture_output=True)
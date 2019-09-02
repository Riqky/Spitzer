import subprocess

def exploit(hosts):
    for host in hosts:
        smbResult = empty(host)

        if 'STATUS_ACCESS_DENIED' in smbResult:
            smbResult = anonymous(host)

        if not 'STATUS_ACCESS_DENIED' in smbResult and not 'STATUS_LOGON_FAILURE' in smbResult:
            print(smbResult + '\n')
        else:
            print('Failed for ' + host + '\n')
        

        

        
def empty(host):
    return subprocess.run(['smbmap', '-H ' + host], capture_output=True).stdout.decode('utf-8')

def anonymous(host):
    return subprocess.run(['smbmap', '-u anonymous', '-H ' + host], capture_output=True).stdout.decode('utf-8')
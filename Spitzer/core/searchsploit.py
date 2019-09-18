from Spitzer.core import command

def find(host, nmap):
    for port, value in nmap[host]['tcp'].items():
        product = value['product']
        version = value['version']

        #check if one is empty
        if product == '':
            continue

        result = command.run(['searchsploit', product, version], True)
        result = result.stdout

        #found no sploits
        if 'Exploits: No Result'in result and 'Shellcodes: No Result' in result:
            continue

        #count found sploits
        count = 0
        for line in result.splitlines():
            if '--------' in line or 'Exploit Title' in line or 'No Result' in line:
                continue
            else:
                count += 1

        s = ''
        if count > 1:
            s = 's'

        print('found ' + str(count) + ' exploit' + s + ' for ' + product + ' ' + version +' on ' + host)
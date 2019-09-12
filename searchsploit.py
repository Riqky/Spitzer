import command

def find(host, nmap):
    for port, value in nmap[host]['tcp'].items():
        product = value['product']
        version = value['version']

        #check if one is empty
        if product == '' or version == '':
            return

        result = command.run(['searchsploit', product, version], True)
        result = result.stdout

        #found no sploits
        if 'Exploits: No Result'in result and 'Shellcodes: No Result' in result:
            return

        #count found sploits
        count = 0
        for line in result.splitlines():
            line = line.split('|')
            if product in line[0] or version in line[0]:
                count += 1

        s = ''
        if count > 1:
            s = 's'

        print('found ' + str(count) + ' exploit' + s + ' for ' + product + ' ' + version +' on ' + host)
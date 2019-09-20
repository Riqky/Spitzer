from Spitzer import command
from Spitzer.result import result

def exploit(url):
    print('nikto')
    cmd = ['nikto', '-host', url]
    '''cmdResult = command.run(cmd, capture_output=True).stdout

    first = False
    secondline = False
    for line in iter(cmdResult.splitlines()):
        if not secondline:
            if line.startswith('-----'):
                if first:
                    first = True
                else:
                    secondline = True #wait for second line (everything after that second line are finds)
        else:
            result.add(line)'''
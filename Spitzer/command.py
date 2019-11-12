import subprocess
import os

from Spitzer.config import config
from Spitzer.print import print_error


#runs shell command
def run(cmd, capture_output=False, check=True, verbose=None):
    if verbose is not None:
        if verbose == -1:
            capture_output = True
        if verbose > 0:
            v = '-'
            for _ in range(verbose):
                v += 'v'
            cmd.append(v)

    #if capture_output is True, print doens't work, sadly...
    print(cmd)
    proc = None
    try:
        proc = subprocess.run(cmd, capture_output=capture_output, check=check, text=True, bufsize=100000)
        return proc.stdout
    except subprocess.SubprocessError:
        print_error('Error in executing ' + cmd[0])
        return None
        #TODO errorlogging

'''def run(command, capture_output=False, check=True):
    pipe = None
    if capture_output:
        pipe = subprocess.PIPE
    process = subprocess.Popen(command, stdout=pipe, text=True, bufsize=1000000)
    code = process.wait()
    if check and code != 0:
        raise RuntimeError('errorcode ' + str(code)) #TODO make custom exceptions

    return process.stdout'''
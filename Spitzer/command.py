import subprocess
import os

from Spitzer.config import config


#runs shell command
def run(command, capture_output=False, check=True, verbose=None):
    print(command)
    if verbose is not None:
        if verbose == -1:
            capture_output = True
        if verbose > 0:
            v = '-'
            for _ in range(verbose):
                v += 'v'
            command.append(v)

    #if capture_output is True, print doens't work, sadly...
    return subprocess.run(command, capture_output=capture_output, check=check, text=True, bufsize=100000).stdout

'''def run(command, capture_output=False, check=True):
    pipe = None
    if capture_output:
        pipe = subprocess.PIPE
    process = subprocess.Popen(command, stdout=pipe, text=True, bufsize=1000000)
    code = process.wait()
    if check and code != 0:
        raise RuntimeError('errorcode ' + str(code)) #TODO make custom exceptions

    return process.stdout'''
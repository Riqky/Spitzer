import subprocess
import os

from Spitzer.config import config


#runs shell command
def run(command, capture_output=False, check=True):
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
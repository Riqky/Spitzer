import subprocess
from config import config

def run(command, capture_output=False, check=True):
    #if capture_output is True, text doens't work, sadly...
    return subprocess.run(command, capture_output=capture_output, check=check, text=config.getStatic('enableOutput'))
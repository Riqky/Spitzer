from Spitzer.core.chache import chache
from Spitzer.core.config import config

def quit(): #runs on exit, for doing cleanup
    chache.clear()
    config.writeStatic()
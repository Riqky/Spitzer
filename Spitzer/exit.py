from Spitzer.chache import chache
from Spitzer.config import config
from Spitzer.print import print

def quit(): #runs on exit, for doing cleanup
    chache.clear()
    config.write_static()
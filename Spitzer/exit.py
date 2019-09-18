from chache import chache
from config import config

def quit(): #runs on exit, for doing cleanup
    chache.clear()
    config.writeStatic()
from core.chache import chache
from core.config import config

def quit(): #runs on exit, for doing cleanup
    chache.clear()
    config.writeStatic()
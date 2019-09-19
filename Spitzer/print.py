from __future__ import print_function
import builtins as __builtin__

def print(*args, **kwargs):
    #is error
    if len(args) != 0 and args[0].startswith('[!]'):
        l = list(args)
        l[0] = '\033[1;31m' + l[0] + '\033[0;37m'
        args = tuple(l)


    return __builtin__.print(*args, **kwargs)
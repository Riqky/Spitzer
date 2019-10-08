import json
from Spitzer.host import get_interfaces
from Spitzer.print import print_error

#handler for the three config files, every setting can the changed here
#TODO make main get rather then static and dynamic (in part with the 'module' system)
#TODO check if interface exsists
path = __file__[:-9]


static = open(path + 'static.json', 'r').read()
static = json.loads(static)

dynamic = open(path + 'dynamic.json', 'r').read()
dynamic = json.loads(dynamic)

data = open(path + 'data.json', 'r').read()
data = json.loads(data)

def get_static(key):
    try:
        value = static[key]
        if value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            return value
        
    except KeyError:
        return None

def get_data(key):
    try: 
        return data[key]
    except KeyError:
        return None

def get_dynamic(key):
    try:
        value = dynamic[key]
        if value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            return value

    except KeyError:
        return None

def set_static(key, value):
    static[key] = value
    
def write_static():
    open(path + 'static.json', 'w').write(json.dumps(static))

def set_dynamic(key, value):
    dynamic[key] = value

def print_config(name='dynamic'):
    if name == 'dynamic':
        printdict(dynamic)
    elif name == 'static':
       printdict(static)
    elif name == 'all':
        print('dynamic')
        print('====================================================================\n')
        printdict(dynamic)
        print('\n')
        print('static')
        print('====================================================================\n')
        printdict(static)
    else:
        print('invalid type')
        print('try: static, dynamic or all')

def printdict(diction):
    for key, value in diction.items():
            if isinstance(value, dict):
                print('\n' + key)
                print('=====================================')
                printdict(value)
            else:    
                spaces = 20*' '
                spaces = spaces[-len(str(value)):]
                print("%-30s %-40s" % (str(key), str(value)))
    print()

def set_value(args):
    key = args[0]
    value = args[1]
    
    if key == 'interface':
        set_ip(value)

    if key in dynamic:
        set_dynamic(key, value)
    elif key in static:
        set_static(key, value)
    else:
        for val in dynamic.items():
            if isinstance(val[1], dict) and key in val[1]:
                dynamic[val[0]][key] = value
                return

        for val in static.items():
            if isinstance(val[1], dict) and key in val[1]:
                static[val[0]][key] = value
                return

        print('key not found')

def get_path():
    return path

def set_ip(interface):
    interfaces = get_interfaces()
    
    if interface is None:
        interface = get_static('interface')

    if interface not in interfaces:
        print_error('[!] Interface not found! make sure you use an exsisting interface')
        return

    set_value(['ip', interfaces[interface]])
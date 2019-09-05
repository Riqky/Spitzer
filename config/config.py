import json

#TODO create .ini file for ports, services and exploit (and alike)

static = open('config/static.json', 'r').read()
static = json.loads(static)

dynamic = open('config/dynamic.json', 'r').read()
dynamic = json.loads(dynamic)

def getStatic(key):
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

def getDynamic(key):
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

def setStatic(key, value):
    static[key] = value
    #write back into the file #TODO? only at shutdown?
    open('config/static.json', 'w').write(json.dumps(static))

def setDynamic(key, value):
    dynamic[key] = value

def printConfig(name='dynamic'):
    if name == 'dynamic':
        printdict(dynamic)
    elif name == 'static':
       printdict(static)
    elif name == 'all':
        printdict(dynamic)
        printdict('\n')
        printdict(static)
    else:
        print('invalid type')
        print('try: static, dynamic or all')

def printdict(diction):
    for key, value in diction.items():
            if isinstance(value, dict):
                print(key)
                print('=========================')
                printdict(value)
            else:    
                print(str(key) + ' : ' + str(value))
    print()

def setValue(args):
    key = args[0]
    value = args[1]

    if getDynamic(key) is not None:
        setDynamic(key, value)
    elif getStatic(key) is not None:
        setStatic(key, value)
    else:
        print('key not found')
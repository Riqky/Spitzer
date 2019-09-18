import json

#handler for the three config files, every setting can the changed here

static = open('lib/config/static.json', 'r').read()
static = json.loads(static)

dynamic = open('lib/config/dynamic.json', 'r').read()
dynamic = json.loads(dynamic)

data = open('lib/config/data.json', 'r').read()
data = json.loads(data)

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

def getData(key):
    try: 
        return data[key]
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
    
def writeStatic():
    open('lib/config/static.json', 'w').write(json.dumps(static))

def setDynamic(key, value):
    dynamic[key] = value

def printConfig(name='dynamic'):
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

def setValue(args):
    key = args[0]
    value = args[1]

    if key in dynamic:
        setDynamic(key, value)
    elif key in static:
        setStatic(key, value)
    else:
        print('key not found')
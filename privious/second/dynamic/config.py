import json

fileName = 'dynamic/config.json'
conf = json.loads(open(fileName, 'r').read())

def printFile():
    for key, diction in conf.items():
        if isinstance(diction, dict):
            print('/n' + key)
            print('===============================================') #TODO? maybe print entire line

            for key, value in diction.items():
                print(str(key) + '  :  ' + str(value))

def editConf(key, value):
    #find correct dict
    diction = None
    for dicti in conf:
        if key in dicti: 

    if diction in conf and key in conf[diction]:
        conf[diction][key] = value
    else:
        print('key or dict not found!')
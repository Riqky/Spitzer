import result
import os
import csv
import json

#results = {}

#test results
results = {
    '127.0.0.1':{
        'findings':[
            'this',
            'that',
            'something'
        ],
        'webpages':[
            'index',
            'main',
            'html'
        ]
    },

    '192.168.1.2':{
        'findings':[
            'asd',
            'fgh',
            'hjk'
        ]
    },
    '10.10.10.10':{
        'webpages':[
            'zxc',
            'bnm',
            'cxvb'
        ]
    }
}

def export():
    global results
    results = result.get()

def exportcsv():
    filefindings = open(os.getcwd() + 'findings.csv', 'w+')
    findingWriter = csv.writer(filefindings)
    filepages = open(os.getcwd() + 'webpages.csv', 'w+')
    pageswriter = csv.writer(filepages)

    for host, value in results.items():
        print(host)
        #print(value)
        if 'findings' in value:
            print(value['findings'])
            findingWriter.writerow([host] + value['findings'])
        if 'webpages' in value:
            print(value['webpages'])
            pageswriter.writerow([host] + value['webpages'])

    print('created ' + os.getcwd() + '/findings.csv')
    print('created ' + os.getcwd() + '/webpages.csv')

def exportjson():
    open(os.getcwd() + 'result.json', 'w+').write(json.dumps(results))
    print('created ' + os.getcwd() + 'result.json')
from Spitzer.result import result
import os
import csv
import json



#results = {}

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

#test results
def export():
    global results
    results = result.get()

def exportcsv():
    file_findings = open(os.getcwd() + 'findings.csv', 'w+')
    finding_writer = csv.writer(file_findings)
    filepages = open(os.getcwd() + 'webpages.csv', 'w+')
    pageswriter = csv.writer(filepages)

    for host, value in results.items():
        if 'findings' in value:
            finding_writer.writerow([host] + value['findings'])
        if 'webpages' in value:
            pageswriter.writerow([host] + value['webpages'])

    print('[-] Created ' + os.getcwd() + '/findings.csv')
    print('[-] Created ' + os.getcwd() + '/webpages.csv')

def exportjson():
    open(os.getcwd() + 'result.json', 'w+').write(json.dumps(results))
    print('[-] Created ' + os.getcwd() + '/result.json')
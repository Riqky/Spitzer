import os
import csv
import json

from Spitzer.result import result
from Spitzer.print import print_error
from Spitzer.command import run

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

def export(arg):
    args = arg.split(' ')

    if args[0] == 'csv':
        exportcsv()
    elif args[0] == 'json':
        exportjson()
    elif args[0] == 'faraday':
        exportfaraday(arg)
    else:
        print_error('[!] No parameter given!')

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



def exportfaraday(arg):
    args = arg.split(' ')
    url = args[1]
    username = args[2]
    password = args[3]
    workspace = args[4]
    
    #TODO generate the csv

    up = username + ':' + password + '@'

    if not url.startswith('https://') and not url.startswith('http://'):
        print_error('[!] Please add http or https')
        return
    if url.startswith('https://'):
        url = url[:8] + up + url[8:]
    else:
        url = url[:7] + up + url[7:]

    cmd = ['faraday-fplugin', 'import_csv', '-u', url, '--csv', 'path', '-w', workspace]

    print(cmd)
    #run(cmd)

    #faraday-fplugin import_csv -u http://username:password@127.0.0.1:5985/ --csv /path/to/file/file.csv -w WORSKPACE_NAME

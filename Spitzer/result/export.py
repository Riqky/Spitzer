from Spitzer.result import result
import os
import csv
import json

from Spitzer.print import print

results = {}

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
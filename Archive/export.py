import os
import csv
import json

from Spitzer.result import result
from Spitzer.print import print_error
from Spitzer.command import run

def export(arg, results):
    args = arg.split(' ')

    if args[0] == 'csv':
        export_csv(results)
    elif args[0] == 'json':
        export_json(results)
    else:
        print_error('[!] No parameter given!')

def export_csv(results):
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

def export_json(results):
    open(os.getcwd() + 'result.json', 'w+').write(json.dumps(results))
    print('[-] Created ' + os.getcwd() + '/result.json')

def export_txt(results):
    txt = ''

    for host, value in results.items():
        if 'findings'  in value:
            print(results[host]['findings'])
            for ob in results[host]['findings']:
                pass#txt += '\n\n' + val['title'] + '\n' + val['text']

        if 'webpages' in value:
            for page in results[host]['webpages']:
                txt +=  '\n\nwebpages\n' + page

    f = open(os.getcwd() + 'results.txt', 'a')
    f.write(txt)
    f.close()
    print('[-] Created ' + os.getcwd() + '/results.txt')
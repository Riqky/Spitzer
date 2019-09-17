import cmd
from exploiters import *
from scanner import scanner
from config import config
import subprocess, shlex
import time 
import os
import importlib
import json
import searchsploit
import exit

#TODO make a 'big' or 'light' switch, cause this program is already a dos'ser

class command(cmd.Cmd):
    intro = 'First Scanner'
    prompt = '> '
    result = {}

    def do_all(self, arg):
        '''runs both the scanner and the exploiter'''
        self.do_scan('')
        self.do_exploit('')

    def do_scan(self, arg):
        '''runs only scanner on the ip(s) given in the config'''
        result = scanner.scan()
        self.result = result

        #print result (mainly for testing)
        for host, value in result.items():
            print(host + ':')
            for port, portVal in value['tcp'].items():
                if portVal['state'] == 'open':
                    print('\t' + str(port) + '  ' + portVal['name'])
            print()
        print('output has been written to ' + os.getcwd() + '/scan.txt')

    def do_exploit(self, arg):
        modules = config.getData('ports')

        for host in self.result:
            searchsploit.find(host, self.result)
            for port in self.result[host]['tcp']:
                module = modules[str(port)][0]
                if module != '':           
                    eval(module + '.exploit(\''+ host +'\', ' + json.dumps(self.result[host]['tcp'][port]) + ',' + str(port) + ')' )
            
    def do_info(self, arg):
        '''shows the config, you can specify the configs dynamic, static or all. dynamic is the standard'''
        if arg is '':
            config.printConfig()
        else:
            config.printConfig(arg)

    def do_set(self, arg):
        '''set the value by the given key'''
        args = arg.split(' ')
        config.setValue(args)

    def do_shell(self, arg):
        '''runs a shell command (!<command> can also be used)'''
        if arg == '': return
        try:
            subprocess.run(shlex.split(arg), text=True) #does something weird with commands like 'cd'  ¯\_(-_-)_/¯
            print()
        except FileNotFoundError:
            print('command not found')

if __name__ == '__main__':
    try:
        command().cmdloop()

    except KeyboardInterrupt:
        print('exiting')
        exit.quit()
    except:
        #print('exiting')
        exit.quit()
        raise
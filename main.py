import cmd
from exploiters import *
from scanner import scanner
from config import config
import subprocess, shlex
import time 
import importlib
import json

#TODO make a 'big' or 'light' switch, cause this program is already a dos'ser

class command(cmd.Cmd):
    intro = 'First Scanner'
    prompt = '> '
    result = {}

    def do_all(self, arg):
        self.do_scan('')
        self.do_exploit('')

    def do_scan(self, arg):
        result = scanner.scan()
        self.result = result

        for host, value in result.items():
            print(host + ':')
            for port, portVal in value['tcp'].items():
                if portVal['state'] == 'open':
                    print('\t' + str(port) + '  ' + portVal['name'])
            print()

    def do_exploit(self, arg):
        modules = config.getData('modules')
        for module in modules:
            eval(module + '.exploit(\''+ config.getDynamic('ip') +'\', ' + json.dumps(self.result) + ')')
            
    def do_info(self, arg):
        if arg is '':
            config.printConfig()
        else:
            config.printConfig(arg)

    def do_set(self, arg):
        args = arg.split(' ')
        config.setValue(args)

    def do_shell(self, arg):
        if arg == '': return
        try:
            subprocess.run(shlex.split(arg), text=True) #does something weird with commands like 'cd'  ¯\_(-_-)_/¯
            print()
        except FileNotFoundError:
            print('command not found')



if __name__ == '__main__':
    command().cmdloop()
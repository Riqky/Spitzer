import cmd
from scanner import scanner
from config import config
import subprocess, shlex
import time 
import os

#TODO make a 'big' or 'light' switch, cause this program is already a dos'ser

class command(cmd.Cmd):
    intro = 'First Scanner'
    prompt = '> '

    def do_scan(self, arg):
        '''runs only scanner on the ip(s) given in the config'''
        result = scanner.scan()

        #print result (mainl for testing)
        for host, value in result.items():
            print(host + ':')
            for port, portVal in value['tcp'].items():
                if portVal['state'] == 'open':
                    print('\t' + str(port) + '  ' + portVal['name'])
            print()
        print('output has been written to ' + os.getcwd() + '/scan.txt')

            
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
    command().cmdloop()
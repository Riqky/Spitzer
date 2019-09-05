import cmd
from exploiters import web
from scanner import scanner
from config import config
import subprocess, shlex
import time

#TODO make a 'big' or 'light' switch, cause this program is already a dos'ser

class command(cmd.Cmd):
    intro = 'First Scanner'
    prompt = '> '

    def do_all(self, arg):
        #TODO scan, exploit for all 'modules'
        #TODO make a list of exploits, for dynamic looping
        i=0#error stopper (fucking python)

    def do_scan(self, arg):
        result = scanner.scan(arg)

        for host, value in result.items():
            print(host + ':')
            for port, portVal in value['tcp'].items():
                if portVal['state'] == 'open':
                    print('\t' + str(port) + '  ' + portVal['name'])
            print()

    def do_exploit(self, arg):
        #web.exploit(config.getDynamic('ip'))
        #TODO as said, make a list of exploits

        #for calling a dynamic method at runtime
        #result = getattr(module, 'method')('params')

        i=0#ugh
            
    def do_info(self, arg):
        config.printFile()

    def do_set(self, arg):
        args = arg.split(' ')
        config.setValue(args)

    def do_shell(self, arg):
        try:
            subprocess.run(shlex.split(arg), text=True) #does something weird with commands like 'cd'  ¯\_(-_-)_/¯
            print()
        except FileNotFoundError:
            print('command not found')

    def do_print(self,arg):
        if arg is '':
            config.printConfig()
        else:
            config.printConfig(arg)



if __name__ == '__main__':
    command().cmdloop()
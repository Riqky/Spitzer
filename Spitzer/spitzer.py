import cmd
import subprocess, shlex
import os
import json
import sys

from lib import searchsploit
from lib import exit
from lib.scanner import scanner
from lib.config import config

#TODO make a 'big' or 'light' switch, cause this program is already a dos'ser
first = True
class command(cmd.Cmd):
    intro = '\nSpitzer\n' if first else '\n'
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
        '''exploits the found results'''
        for host in self.result:
            searchsploit.find(host, self.result)

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

    def do_exit(self, arg):
        '''exits the application'''
        exit.quit()
        sys.exit()
    def do_quit(self, arg):
        '''exits the application'''
        exit.quit()
        sys.exit()
    def do_q(self, arg):
        '''exits the application'''
        exit.quit()
        sys.exit()


def main():
    global first
    try:
        c = command()
        if not first:
            c.intro = '\n'
        c.cmdloop()

    except KeyboardInterrupt:
        first = False
        main()
    except:
        exit.quit()
        raise

if __name__ == "__main__":
    main()
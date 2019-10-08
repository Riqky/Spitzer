import cmd
import subprocess, shlex
import os
import json
import sys

from Spitzer import searchsploit
from Spitzer import exit
from Spitzer.scanner import scanner
from Spitzer.config import config
from Spitzer.print import print_error

#TODO make a 'big' or 'light' switch, cause this program is already a dos'ser
first = True
class Command(cmd.Cmd):
    intro = '''
    
 _____       _ _                
/  ___|     (_) |               
\\ `--. _ __  _| |_ _______ _ __ 
 `--. \\ '_ \\| | __|_  / _ \\ '__|
/\\__/ / |_) | | |_ / /  __/ |   
\\____/| .__/|_|\\__/___\\___|_|   
      | |                       
      |_|                       

    
          ooo
         / : \\
        / o0o \\
  _____"~~~~~~~"_____
  \\+###|U * * U|###+/
   \\...!(.>..<)!.../
    ^^^^o|   |o^^^^
#+=====}:^^^^^:{=====+#
 .____  .|!!!|.  ____.
 |#####:/" " "\\:#####|
 |#####=|  O  |=#####|
 |#####>\\_____/<#####|
  ^^^^^   | |   ^^^^^
          o o
'''
    prompt = '> '
    result = {}
    config.set_ip(None)

    def do_all(self, arg):
        '''runs both the scanner and the exploiter'''
        self.do_scan('')
        self.do_exploit('')

    def do_scan(self, arg):
        '''runs only scanner on the ip(s) given in the config'''
        result = scanner.scan()
        self.result = result

        if result is None:
            return

        #print result (mainly for testing)
        for host, value in result.items():
            print(host + ':')
            for port, port_val in value['tcp'].items():
                if port_val['state'] == 'open':
                    print('\t' + str(port) + '  ' + port_val['name'])
            print()
        print('[-] Output has been written to ' + os.getcwd() + '/scan.txt')
            
    def do_exploit(self, arg):
        '''exploits the found results'''
        for host in self.result:
            searchsploit.find(host, self.result)

    def do_info(self, arg):
        '''shows the config, you can specify the configs dynamic, static or all. dynamic is the standard'''
        if arg is '':
            config.print_config()
        else:
            config.print_config(arg)

    def do_set(self, arg):
        '''set the value by the given key'''
        args = arg.split(' ')
        config.set_value(args)

    def completedefault(self, text, line, begidx, endidx):
        if text == 'i':
            return ['ip', 'interface']
        if text == 'in':
            return ['interface']

    def do_shell(self, arg):
        '''runs a shell command (!<command> can also be used)'''
        if arg == '': return
        try:
            subprocess.run(shlex.split(arg), text=True) #does something weird with commands like 'cd'  ¯\\_(-_-)_/¯
            print()
        except FileNotFoundError:
            print_error('[!] Command not found')

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
    def do_EOF(self, arg):
        '''exits the application'''
        exit.quit()
        sys.exit()

    def emptyline(self):
        pass


def main():
    global first
    try:
        c = Command()
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
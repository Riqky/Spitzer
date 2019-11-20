import cmd
import subprocess, shlex
import os
import json
import sys

from Spitzer import searchsploit, exit 
from Spitzer.scanner import scanner
from Spitzer.config import config
from Spitzer.result import result
from Spitzer.exploiters.exploit import exploit
from Spitzer.print import print_error, print_warning

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
    result = {} #TODO fix when scan and exploit are run

    config.set_ip(None)

    def do_run(self, arg):
        '''runs both the scanner and the exploiter'''
        self.do_scan('')
        self.do_exploit('')

    def do_scan(self, arg):
        '''runs only scanner on the ip(s) given in the config'''
        self.result = scanner.scan()

        if self.result is None:
            return

        result.save_hosts(self.result)
        #print result (mainly for testing)
        for host, value in self.result.items():
            print(host + ':')
            for port, port_val in value['tcp'].items():
                if port_val['state'] == 'open':
                    print('\t' + str(port) + '  ' + port_val['name'])
            print()
        print('[-] Output has been written to ' + os.getcwd() + '/scan.txt')
            
    def do_exploit(self, arg):
        '''exploits the found results'''

        #for host in self.result:
         #   searchsploit.find(host, self.result)
        exploit(self.result)

    def do_options(self, arg):
        '''shows the config.'''
        config.print_config()

    def do_set(self, arg):
        '''set the value by the given key'''
        args = arg.split(' ')
        config.set_value(args)

    def complete_set(self, text, line, begidx, endidx):
        return config.complete_key(text)

    def do_shell(self, arg):
        '''runs a shell command (!<command> can also be used)'''
        if arg == '': return
        try:
            subprocess.run(shlex.split(arg), text=True) #does something weird with commands like 'cd'  ¯\_(-_-)_/¯
            print()
        except FileNotFoundError:
            print_error('Command not found')

    def do_exit(self, arg):
        '''exits the application'''
        exit.quit()
        sys.exit()
    def do_quit(self, arg):
        '''exits the application'''
        exit.quit()
        sys.exit()
    def do_EOF(self, arg):
        '''exits the application (for CTRL+D)'''
        exit.quit()
        sys.exit()

    def emptyline(self):
        pass
    
    def do_export(self, arg):
        export()

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
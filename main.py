import cmd
from scanner import scanner
import smb

#TODO create config file
#TODO create settings system

class command(cmd.Cmd):
    intro = 'SMBMapper'
    prompt = 'map > '

    #TODO not only smb
    #def do_scan(self, arg):


    def do_smb(self, arg):
        hosts = scanner.scanSMB(arg)
        if hosts is not None:
            smb.exploit(hosts)
        else:
            print('None of the specified hosts is up or runnnig smb')
            




if __name__ == '__main__':
    command().cmdloop()
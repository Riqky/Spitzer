import cmd
import smb
import web
from scanner import scanner
from dynamic import config

#TODO create config file
#TODO create settings system

class command(cmd.Cmd):
    intro = 'SMBMapper'
    prompt = 'map > '

    def do_smb(self, arg):
        hosts = scanner.scan(arg, 445, 'microsoft-ds')
        if hosts is not None:
            smb.exploit(hosts)
        else:
            print('None of the specified hosts is up or runnnig smb')
            
    def do_info(self, arg):
        config.printFile()

    def do_web(self, arg):
        hosts = scanner.scan(arg, [80,443], alias='web')

        if hosts is not None:
            web.exploit(hosts)

    def do_set(self, arg):
        args = arg.split(' ')
        #config.editConf()



if __name__ == '__main__':
    command().cmdloop()
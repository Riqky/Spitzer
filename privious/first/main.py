import cmd
import help
import scanner
import methods

class command(cmd.Cmd):
    intro = 'Zero Day Wrapper \n'
    prompt = '> '

    options = {
        'thread': 5,
        'dict' : {
            'test': 1
        }
    }

    def do_help(self, arg):
        help.help(self, arg, cmd.Cmd)

    def do_scan(self, arg):
        scanner.scan('192.168.192.133')
        print(scanner.getState('192.168.192.133'))

    def do_set(self, arg):
        if not arg:
            print('no parameters given!')
            return

        args = arg.split(' ')

        if len(args) < 2:
            print('no value given!')
            return

        try:
            args[1] = type(self.options[args[0]])(args[1])
        except ValueError:
            print('argument is in wrong type')
            return
        except KeyError:
            print('key is not found')
            return

        self.options[args[0]] = args[1]

    def do_options(self, arg):
        methods.printDict(self, self.options)

if __name__ == '__main__':
    while True:
        try:
            command().cmdloop()
        except KeyboardInterrupt:
            print('')
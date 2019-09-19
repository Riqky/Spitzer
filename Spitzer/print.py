
def print_error(text):
    #is error
    if text.startswith('[!]'):
        text = '\033[1;31m' + text + '\033[0;37m'

    print(text)
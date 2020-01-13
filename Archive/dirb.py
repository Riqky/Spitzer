def dirb(host, wordlist):
    print('starting dirb')

    cmd = ['dirb', host, config.get_config('busterlist')[wordlist], '-w']
    completed = command.run(cmd, capture_output=True)

    pages = []
    for line in iter(completed.stdout.splitlines()):
        #correct page: + http://10.10.10.146/uploads/index.html (CODE:200|SIZE:2)
        if line.startswith('+ ') and 'CODE:200' in line:
            #remove '+ '
            line = line[2:]

            while ' ' in line:
                line = line[:-1] #remove 1 char until spaces are gone

            pages.append(line)
    result.add_pages(host, pages)
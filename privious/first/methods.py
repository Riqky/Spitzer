def printDict(self, items):
    for item, value in items.items():
        if isinstance(value, dict):
            print(item + ':')
            printDict(self, value)

        else:
            print(item + ' : ' + str(value))
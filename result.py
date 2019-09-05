webpages = []

def addPage(page):
    global webpages
    webpages.append(page)

def addPages(pages):
    global webpages
    webpages += pages
    print(webpages)
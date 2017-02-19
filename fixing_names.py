with open('names.txt', 'r', encoding="utf8") as fileNames:
    name_restrictions = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    names = fileNames.read().splitlines()
    newnames = []
    for name in names:
        for restriction in name_restrictions:
            if(restriction in name):
                name = name.replace(restriction, '')
        if(not(name == ' ' or name == '')):
            newnames.append(name)
    
with open('names.txt', 'w', encoding="utf8") as fileNames:
    for n in newnames:
	    fileNames.write(n + '\n')

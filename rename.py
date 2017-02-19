import os
with open('names.txt', 'r', encoding="utf8") as fileNames:
    names = fileNames.read().splitlines()
    for ind, name in enumerate(names):
        old_name = str(ind + 1) + '.mp4'
        new_name = str(ind + 1).zfill(3) + '_' + name.replace(' ', '_') + '.mp4'
        try:
            os.rename(old_name, new_name)
        except:
            continue
    




import os
import glob
import shutil
f = glob.glob('zadanie1/*')
print(f)

l = []

for elements in f:
    print(elements.split('\\')[1])
    name = elements.split('\\')[1][0]
    source_file = 'zadanie1/' + elements.split('\\')[1]
    if name in l:
        pass
    else:
        try:
            os.mkdir(name)
            l.append(name)
        except FileExistsError:
            pass
    shutil.move(source_file, name + '/')

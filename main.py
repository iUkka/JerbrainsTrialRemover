import os, fnmatch, shutil

rootDir = os.getenv("HOME")
pattern = ".PyCharm*"
listOfFiles = os.listdir(rootDir)

for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        remove = os.path.join(rootDir,entry,"config/eval")
        if os.path.exists(remove):
            shutil.rmtree(remove)


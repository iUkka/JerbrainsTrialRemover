import os, fnmatch, shutil

rootDir = os.getenv("HOME")
pattern = ".PyCharm*|.GoLang"

for entry in os.listdir(rootDir):
    if fnmatch.fnmatch(entry, pattern):
        remove = os.path.join(rootDir,entry,"config/eval")
        if os.path.exists(remove):
            shutil.rmtree(remove)


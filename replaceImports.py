#!/usr/bin/python

import re, sys, os

importRegex = re.compile("<(?:import|include) [\"']?([\\w\\d./()+\-\s]+)[\"']? />")

def readAndPrint(filename, path):
    if(not filename.startswith("/")):
        filename = str(path) + "/" + filename
        
    with open(filename) as f:
        for line in f:
            imports = importRegex.findall(line)
            if (len(imports) > 0):
                print(importRegex.sub("", line).strip())
                for imported in imports:
                    readAndPrint(imported, os.path.dirname(os.path.realpath(f.name)))
            else:
                print(line.strip())
        

if(len(sys.argv) <= 0):
    print " usage: replaceImports.py <file 1> [file 2] ..."
    print ""
    print " This program will print the contents of all files given to it, but will replace, for instance, <import \"blah.py\"> (starting at the < character) with a new line and the contents of blah.py."
    print "You can use paths to the included files; if those paths starts with a /, they are considered absolute, otherwise they are relative to the file currently being imported."
    print "You can import in an imported file; the only real limitation to how many imports 'deep' you can go is your file descriptors, I think."
    print "Hope this helps!"
else:
    first = True
    for filename in sys.argv:
        if(first):
            first = False
        else:
            readAndPrint(filename, os.getcwd())

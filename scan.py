import os
import sys
import re
re_a = re.compile(r"(.+)\(.+\)\.(exe|EXE)")
re_b = re.compile(r"(.+)\.(exe|EXE)")

def getName(fileName):
    if m:=re_a.match(fileName):
        return m.group(1)
    elif m:=re_b.match(fileName):
        return m.group(1)
    else:
        return fileName

contentf = """{}
  file: {}
  path: 
"""

if len(sys.argv) < 2:
    sys.stderr.write(f"Usage : {sys.argv[0]} [dir]\n")
    
elif os.path.isdir(sys.argv[1]):
    file_list = os.listdir(sys.argv[1])
    for fname in file_list:
        name = getName(fname)

        print(contentf.format(fname, name))
    
else:
    sys.stderr.write(f"{sys.argv[1]} : no such directory\n")
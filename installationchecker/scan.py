import os
import sys
import re
RE_EXECUTE = re.compile(r"^(.+?)(\(.+\))?[.](exe|EXE|msi|MSI)$")

def get_name(fileName):
    if m:=RE_EXECUTE.match(fileName):
        return m.group(1)
    else:
        return fileName

def scan(path:str):
    file_list = os.listdir(path)
    content_format = "{}\n"
    content_format += "    file: {}\n"
    content_format += "    path:\n"

    for fname in file_list:
        name = get_name(fname)
        print(content_format.format(fname, name))
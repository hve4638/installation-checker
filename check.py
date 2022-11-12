import os
import yaml
import re
from colorama import Fore, Style

RE_ENV = re.compile("%([a-zA-Z_]+)%")
def parsePath(path:str)->str:
    fullPath = ""

    path_items = path.replace("/", "\\").split("\\")
    for part in path_items:
        if not len(part):
            continue
        elif m := RE_ENV.match(part):
            env = os.environ[m.group(1)]
            fullPath += f"{env}\\"
        else:
            fullPath += f"{part}\\"
    return fullPath

def isInstalled(path:str|None)->bool:
    if path is None:
        return False
    elif os.path.exists(path):
        return True
    else:
        return False

with open('list.yaml') as f:
    ls = yaml.load(f, Loader=yaml.FullLoader)

for name, item in ls.items():
    if item['path'] is None:
        print(f"{Fore.YELLOW} [-] {Style.RESET_ALL} {name}")
        continue

    path = parsePath(item['path'])
    if isInstalled(path):
        print(f"{Fore.GREEN} [V] {Style.RESET_ALL} {name}")
    else:
        print(f"{Fore.RED} [X] {Style.RESET_ALL} {name}")

os.system("pause")
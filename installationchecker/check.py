import os
import yaml
import re
from colorama import Fore, Style

RE_ENV = re.compile("%([a-zA-Z_]+)%")

def parse_path(path:str)->str:
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

def is_installed(path:str|None)->bool:
    if path is None:
        return False
    elif os.path.exists(path):
        return True
    else:
        return False

def check(file_name:str):
    installed:list[str] = []
    not_installed:list[str] = []
    unknown:list[str] = []

    with open(file_name) as f:
        ls = yaml.load(f, Loader=yaml.FullLoader)
        
    while True:
        os.system("cls")
        unknown.clear()
        installed.clear()
        not_installed.clear()

        for name, item in ls.items():
            if item['path'] is None:
                unknown.append(name)
            elif is_installed(parse_path(item['path'])):
                installed.append(name)
            else:
                not_installed.append(name)

        for name in installed:
            print(f"{Fore.GREEN} [V] {Style.RESET_ALL} {name}")
        for name in not_installed:
            print(f"{Fore.RED} [X] {Style.RESET_ALL} {name}")
        for name in unknown:
            print(f"{Fore.YELLOW} [-] {Style.RESET_ALL} {name}")

        os.system("pause")
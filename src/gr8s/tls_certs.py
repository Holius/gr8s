import os
import sys
import subprocess
from gr8s.cli import CLIMenu
from functools import partial
from typing import Dict, List

def read_from_fd(fd: int):
    content = []
    while True:
        chunk = os.read(fd, 512)  # Read in chunks of 1024 bytes
        if not chunk:  # If chunk is empty, EOF is reached
            break
        content.append(chunk)
    
    return b''.join(content).decode('utf-8')  # Join all chunks and decode to a string

def substring(string: str, substrings: List[str]) -> bool:
    for ss in substrings:
        if ss in string:
            return True
    return False

def cli_mapper(cli_raw: str) -> Dict[str, str]:
    cli_arg_to_filepath = {}
    for t in cli_raw.split(" "):
        if t.startswith("--"):
            cli_arg, path =t.split("=")
            if substring(cli_arg, ["-ca", "cert", "key"]):
                cli_arg_to_filepath[cli_arg.removeprefix("--")] = path
    return cli_arg_to_filepath

def display_cert(filepath: str) -> str:
    try:
        command = ["openssl", "x509", "-in", filepath, '-text', '-noout' ]
        sp_out = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        out = "STDOUT recieved no output"
        if sp_out.stderr is not None:
            fd = sp_out.stderr.fileno()
            out = read_from_fd(fd)
            if out == "":
                if sp_out.stdout is not None:
                    fd = sp_out.stdout.fileno()
                    out = read_from_fd(fd)
        return out
    except Exception as e:
        return str(e)

def view_certs():
    input = ""
    if len(sys.argv) > 1:
        input = sys.argv[1]
    if input == "":
        print("Pass into string to parse")
        return

    tls_raw: str = input
    cli_arg_to_filepath = cli_mapper(tls_raw)
    menu_mapper = {}
    for cli_arg, filepath in cli_arg_to_filepath.items():
        option = f"{cli_arg} > {filepath}"
        c = partial(display_cert, filepath)
        menu_mapper[option] = c

    cm = CLIMenu(menu_mapper)
    cm.display()

    



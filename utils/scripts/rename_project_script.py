#!/usr/bin/python
import subprocess
import sys
from pathlib import Path
import os

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_NAME = os.environ.get("PROJECT_NAME")


def rename_project(name: str):
    # FIXME
    if PROJECT_NAME:
        command = ["mv", BASE_DIR / PROJECT_NAME, BASE_DIR / name]

        try:
            subprocess.run(command)
        except:
            print("Environment variable PROJECT_NAME is not a directory")

        upate_env_file(name)
    else:
        print("Environment variable PROJECT_NAME is not defined")


def upate_env_file(name: str):
    ENV_FILE = BASE_DIR / ".env"
    ENV_FILE.touch(exist_ok=True)

    with open(ENV_FILE, "r") as f:
        lines = f.readlines()

    KEYWORD = "PROJECT_NAME="
    VALUE = f"PROJECT_NAME='{name}'\n"

    if any([KEYWORD in i for i in lines]):
        for index, line in enumerate(lines):
            if KEYWORD in line.replace(" ", ""):
                lines[index] = VALUE
    else:
        lines.append(VALUE)

    with open(ENV_FILE, "w") as f:
        f.writelines(lines)

#!/usr/bin/python
import os
import subprocess
import sys
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).parent
PROJECT_NAME = os.environ.get("PROJECT_NAME")


def rename_project(name: str):
    # FIXME
    if PROJECT_NAME:
        command = ["mv", BASE_DIR / PROJECT_NAME, BASE_DIR / name]

        try:
            subprocess.run(command)
            upate_env_file(name)
        except:
            print("Environment variable PROJECT_NAME is not a directory")

    else:
        print("Environment variable PROJECT_NAME is not defined")


def upate_env_file(name: str):
    ENV_FILE = BASE_DIR / ".env"
    ENV_FILE.touch(exist_ok=True)

    with open(ENV_FILE, "r") as f:
        lines = f.readlines()

    KEYWORD = "PROJECT_NAME="
    VALUE = f"\nPROJECT_NAME='{name}'\n"

    if any([KEYWORD in i.replace(" ", "") for i in lines]):
        for index, line in enumerate(lines):
            if KEYWORD in line.replace(" ", ""):
                lines[index] = VALUE
    else:
        lines.append(VALUE)

    with open(ENV_FILE, "w") as f:
        f.writelines(lines)

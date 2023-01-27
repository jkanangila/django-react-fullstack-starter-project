#!/usr/bin/python
import subprocess
import sys
from pathlib import Path


def generate_erd():
    commands = [
        "mkdir -p __erd__",
        "python manage.py graph_models -a -g --arrow-shape normal --color-code-deletions -o __erd__/erd.dot",
        "python manage.py graph_models -a -g --arrow-shape normal --color-code-deletions -o __erd__/erd.png",
    ]
    for commnand in commands:
        subprocess.run(commnand.split(" "))


def rename_project():
    pass

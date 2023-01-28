#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

from utils import USER_DEFINED_SCRIPTS, utils_scripts_resolver

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent

PROJECT_NAME = os.environ.get("PROJECT_NAME")
if not PROJECT_NAME:
    raise RuntimeError("Environment variable PROJECT_NAME not set")
SETTINGS_MODULE = f"{PROJECT_NAME}.settings"


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] in USER_DEFINED_SCRIPTS:
        utils_scripts_resolver(sys.argv)
    else:
        main()

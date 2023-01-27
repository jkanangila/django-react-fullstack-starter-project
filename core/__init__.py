import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

PROJECT_NAME = os.environ.get("PROJECT_NAME")
SETTINGS_MODULE = f"{PROJECT_NAME}.settings"

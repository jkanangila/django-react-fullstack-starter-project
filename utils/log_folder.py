from os import environ
from pathlib import Path

from django.conf import settings

def get_log_folder_path(environment: str):
    if environment == "dev":
        LOGS_DIRECTORY = settings.BASE_DIR / 'logs' / 'dj.log'
        if not LOGS_DIRECTORY.parent.is_dir():
            LOGS_DIRECTORY.parent.mkdir(exist_ok=True)
    else:
        LOGS_DIRECTORY = Path(environ.get("LOGS_DIRECTORY", '/random-folder/fake.foo'))

        if not LOGS_DIRECTORY.parent.is_dir():
            raise IsADirectoryError('The specified LOGS_DIRECTORY is not a directory')

    return LOGS_DIRECTORY

"""A script that's needed to setup django if it's not already running on a server.
It allows interactions with django's queryset in every python file it's imported in.
"""
import os
import sys

import django

from manage import SETTINGS_MODULE

# Find the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project base directory to the sys.path
# This means the script will look in the base directory for any module imports
# Therefore you'll be able to import analysis.models etc
sys.path.insert(0, BASE_DIR)

# The DJANGO_SETTINGS_MODULE has to be set to allow us to access django imports
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

#  Allow queryset filtering asynchronously when running in a Jupyter notebook
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# This is for setting up django
django.setup()

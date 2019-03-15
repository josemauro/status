"""Module to test the napp kytos/mef_eline."""
import sys
import os
from pathlib import Path

if 'VIRTUAL_ENV' in os.environ:
    BASE_ENV = Path(os.environ['VIRTUAL_ENV'])
else:
    BASE_ENV = Path('/')

#STATUS_NAPP_PATH = BASE_ENV / '/var/lib/kytos/napps/..'

STATUS_NAPP_PATH = str(BASE_ENV) + '/var/lib/kytos/'

sys.path.insert(0, str(STATUS_NAPP_PATH))

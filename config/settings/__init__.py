from __future__ import absolute_import, unicode_literals

import os
from pathlib import Path
import environ

# Load .env
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # <-- fix this line
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Load environment-specific settings
ENVIRONMENT = env('ENVIRONMENT', default='dev').lower()

if ENVIRONMENT == 'prod':
    from .prod import *
    print(f'Current Environment: {ENVIRONMENT}')
elif ENVIRONMENT == 'dev':
    from .dev import *
    print(f'Current Environment: {ENVIRONMENT}')
else:
    raise ValueError(f"Invalid ENVIRONMENT: {ENVIRONMENT}. Must be 'dev' or 'prod'.")

import os

if 'VIRTUAL_ENV' in os.environ:
    print('Virtual environment is currently activated.')
else:
    print('Virtual environment is not activated.')

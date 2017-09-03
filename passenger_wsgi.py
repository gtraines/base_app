import os
import sys

HOME = os.environ.get('HOME')

VENV = HOME + '/anaconda3/envs/appenv35'
PYTHON_BIN = VENV + '/bin/python3'
INTERP = PYTHON_BIN

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, '{v}/lib/python3.5/site-packages'.format(v=VENV))
from app_start import app
from app_start import initialize_app
application = initialize_app(app)
application.config['SERVER_NAME'] = ''

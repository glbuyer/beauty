#!/usr/bin/python
import os
import sys

# pip install virtualenv
# pip install -r requirements.txt
activate_this = '/root/beauty/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

path = os.path.join(os.path.dirname(__file__), os.pardir)
if path not in sys.path:
    sys.path.append(path)

sys.path.insert(0, '/var/www/beauty.com/')
from server import server as application
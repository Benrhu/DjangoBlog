import os
from django.core.wsgi import get_wsgi_application
from gunicorn.app.wsgiapp import run

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogWithPython.settings')

application = get_wsgi_application()

activate_this = '/var/www/grouzy.com/html/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
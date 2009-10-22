import os, sys

sys.path.append('/tmp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ui.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()


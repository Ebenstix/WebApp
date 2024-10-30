
import os
import sys

sys.path.insert(0, 'multimedia_site')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_site.settings')

application = get_wsgi_application()

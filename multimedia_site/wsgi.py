
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, 'multimedia_site')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_site.settings')

application = get_wsgi_application()

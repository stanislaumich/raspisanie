import sys, os 
cwd = os.getcwd() 
sys.path.append(cwd) 
sys.path.append(cwd + '/raspisanie') 
os.environ['DJANGO_SETTINGS_MODULE'] = "raspisanie.settings" 
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()
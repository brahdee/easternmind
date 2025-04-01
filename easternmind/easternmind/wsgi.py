from pathlib import Path

import os
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easternmind.settings")
BASE_DIR = Path(__file__).resolve().parent.parent

if settings.DEBUG:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = WhiteNoise(get_wsgi_application(), root=BASE_DIR / "assets/")

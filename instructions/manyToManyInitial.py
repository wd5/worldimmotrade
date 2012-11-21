# Use in dreampie
# Insert initial data for chices

import sys
sys.path.append('/srv/http/immotrade/')
import settings
from django.core.management import setup_environ
setup_environ(settings)
from django.conf import settings
settings.ADMINS

from estates.models import *
for m in models.get_models():
    if hasattr(m, "use_list"):
        for k,v in m.use_list:
            a=m(options=k)
            a.save()
